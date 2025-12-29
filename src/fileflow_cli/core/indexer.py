"""File indexing system for FileFlowCLI."""

import hashlib
import os
from pathlib import Path
from typing import Dict, Any, Optional, List, Iterator
from datetime import datetime

from ..storage.checkpoint_manager import CheckpointManager
from ..utils.error_handler import handle_error, IndexingError
from .parallel_executor import ParallelExecutor
from ..utils.config import get_config


class FileIndexer:
    """Indexes files and directories."""
    
    def __init__(self, config_dir: Path):
        """
        Initialize file indexer.
        
        Args:
            config_dir: Path to .fileflow_cli directory
        """
        self.config_dir = Path(config_dir)
        self.checkpoint_manager = CheckpointManager(self.config_dir)
        self.batch_size = get_config("batch_size", 100)
        self.thread_count = get_config("thread_count", 4)
        self.executor = ParallelExecutor(max_workers=self.thread_count)
    
    def index_directory(
        self,
        directory: Path,
        checkpoint: Optional[Dict[str, Any]] = None
    ) -> Iterator[Dict[str, Any]]:
        """
        Index directory recursively with parallel processing.
        
        Args:
            directory: Directory to index
            checkpoint: Optional checkpoint data to resume from
        
        Yields:
            Progress update dictionaries
        """
        directory = Path(directory).resolve()
        
        if not directory.exists() or not directory.is_dir():
            raise IndexingError(f"Directory does not exist: {directory}")
        
        # Collect all files to process
        all_files = self._collect_files(directory)
        total_files = len(all_files)
        
        # Determine starting point from checkpoint
        start_index = 0
        processed_paths = []
        file_hashes = {}
        
        if checkpoint:
            processed_paths = checkpoint.get("processed_paths", [])
            file_hashes = checkpoint.get("file_hashes", {})
            start_index = len(processed_paths)
        
        # Prepare progress data
        started_at = checkpoint.get("started_at") if checkpoint else datetime.now().isoformat()
        
        # Process files in batches
        total_batches = (total_files - start_index + self.batch_size - 1) // self.batch_size
        
        for batch_num in range((start_index // self.batch_size) + 1, total_batches + 1):
            batch_start = start_index + (batch_num - 1) * self.batch_size
            batch_end = min(batch_start + self.batch_size, total_files)
            batch_files = all_files[batch_start:batch_end]
            
            # Process batch in parallel
            tasks = [
                lambda f=file: self._process_file(f, directory)
                for file in batch_files
            ]
            
            batch_results = self.executor.execute_parallel(
                tasks,
                callback=lambda completed, result: None  # Progress handled via yield
            )
            
            # Collect results
            for result in batch_results:
                if result:
                    processed_paths.append(result["path"])
                    file_hashes[result["path"]] = result["hash"]
            
            # Save checkpoint
            progress_data = {
                "started_at": started_at,
                "total_files": total_files,
                "processed_files": len(processed_paths),
                "processed_paths": processed_paths,
                "file_hashes": file_hashes,
                "current_batch": batch_num,
                "total_batches": total_batches,
                "status": "in_progress"
            }
            
            self.checkpoint_manager.save_checkpoint(progress_data)
            
            # Yield progress update
            yield {
                "total_files": total_files,
                "processed_files": len(processed_paths),
                "current_batch": batch_num,
                "total_batches": total_batches,
                "progress_percent": (len(processed_paths) / total_files * 100) if total_files > 0 else 0
            }
        
        # Clear checkpoint when complete
        self.checkpoint_manager.clear_checkpoint()
        
        # Final yield
        yield {
            "total_files": total_files,
            "processed_files": len(processed_paths),
            "current_batch": total_batches,
            "total_batches": total_batches,
            "progress_percent": 100.0,
            "complete": True
        }
    
    def resume_indexing(self, directory: Path) -> Iterator[Dict[str, Any]]:
        """
        Resume indexing from checkpoint.
        
        Args:
            directory: Directory to index
        
        Yields:
            Progress update dictionaries
        """
        checkpoint = self.checkpoint_manager.load_checkpoint()
        if not checkpoint:
            # No checkpoint, start fresh
            yield from self.index_directory(directory)
        else:
            # Resume from checkpoint
            yield from self.index_directory(directory, checkpoint)
    
    def _collect_files(self, directory: Path) -> List[Path]:
        """
        Collect all files to index recursively.
        
        Args:
            directory: Directory to scan
        
        Returns:
            List of file paths
        """
        files = []
        
        try:
            for item in directory.rglob("*"):
                if item.is_file():
                    # Skip files without read permissions
                    if os.access(item, os.R_OK):
                        files.append(item)
                    # Skip .fileflow_cli directory
                    elif ".fileflow_cli" in str(item):
                        continue
        except PermissionError as e:
            # Handle permission errors gracefully
            handle_error(e, {"operation": "collect_files", "directory": str(directory)})
        
        return sorted(files)
    
    def _process_file(self, file_path: Path, base_directory: Path) -> Optional[Dict[str, Any]]:
        """
        Process a single file and extract metadata.
        
        Args:
            file_path: Path to file
            base_directory: Base directory for relative paths
        
        Returns:
            Dictionary with file metadata or None if error
        """
        try:
            # Get relative path
            try:
                relative_path = file_path.relative_to(base_directory)
            except ValueError:
                relative_path = file_path
            
            # Get file stats
            stat = file_path.stat()
            
            # Calculate file hash (for change detection)
            file_hash = self._calculate_file_hash(file_path)
            
            # Get file extension
            suffix = file_path.suffix.lower()
            
            return {
                "path": str(relative_path),
                "name": file_path.name,
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "hash": file_hash,
                "extension": suffix,
                "is_directory": False
            }
        
        except Exception as e:
            # Handle errors gracefully
            handle_error(e, {"operation": "process_file", "file": str(file_path)})
            return None
    
    def _calculate_file_hash(self, file_path: Path, chunk_size: int = 8192) -> str:
        """
        Calculate SHA256 hash of file (surface-level, reads first chunk only for large files).
        
        Args:
            file_path: Path to file
            chunk_size: Size of chunk to read (default: 8KB)
        
        Returns:
            SHA256 hash string
        """
        hash_obj = hashlib.sha256()
        
        try:
            with open(file_path, "rb") as f:
                # Read first chunk for quick hash (surface-level analysis)
                chunk = f.read(chunk_size)
                hash_obj.update(chunk)
                
                # For small files, read the rest
                if len(chunk) == chunk_size:
                    # Large file - only hash first chunk + metadata
                    stat = file_path.stat()
                    hash_obj.update(str(stat.st_size).encode())
                    hash_obj.update(str(stat.st_mtime).encode())
                else:
                    # Small file - read everything
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        hash_obj.update(chunk)
        except (IOError, PermissionError):
            # If can't read, use path + modified time as hash
            try:
                stat = file_path.stat()
                hash_obj.update(str(file_path).encode())
                hash_obj.update(str(stat.st_mtime).encode())
            except:
                hash_obj.update(str(file_path).encode())
        
        return hash_obj.hexdigest()

