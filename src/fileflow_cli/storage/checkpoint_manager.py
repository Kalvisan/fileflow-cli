"""Checkpoint management system for FileFlowCLI."""

import json
import hashlib
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime


class CheckpointManager:
    """Manages checkpoints for indexing operations."""
    
    CHECKPOINT_VERSION = "1.0"
    CHECKPOINT_FILENAME = "index_checkpoint.json"
    
    def __init__(self, config_dir: Path):
        """
        Initialize checkpoint manager.
        
        Args:
            config_dir: Path to .fileflow_cli directory
        """
        self.config_dir = Path(config_dir)
        self.checkpoint_file = self.config_dir / self.CHECKPOINT_FILENAME
    
    def save_checkpoint(
        self,
        progress_data: Dict[str, Any],
        validate: bool = True
    ) -> bool:
        """
        Save checkpoint to disk.
        
        Args:
            progress_data: Progress data dictionary
            validate: Whether to validate checkpoint before saving
        
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            # Ensure config directory exists
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
            # Prepare checkpoint data
            checkpoint = {
                "checkpoint_version": self.CHECKPOINT_VERSION,
                "started_at": progress_data.get("started_at", datetime.now().isoformat()),
                "last_updated": datetime.now().isoformat(),
                "total_files": progress_data.get("total_files", 0),
                "processed_files": progress_data.get("processed_files", 0),
                "processed_paths": progress_data.get("processed_paths", []),
                "file_hashes": progress_data.get("file_hashes", {}),
                "current_batch": progress_data.get("current_batch", 0),
                "total_batches": progress_data.get("total_batches", 0),
                "status": progress_data.get("status", "in_progress")
            }
            
            # Calculate integrity hash
            checkpoint["integrity_hash"] = self._calculate_integrity_hash(checkpoint)
            
            # Save to file
            with open(self.checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint, f, indent=2, ensure_ascii=False)
            
            return True
        
        except (IOError, json.JSONEncodeError) as e:
            print(f"Error saving checkpoint: {e}")
            return False
    
    def load_checkpoint(self, validate: bool = True) -> Optional[Dict[str, Any]]:
        """
        Load checkpoint from disk.
        
        Args:
            validate: Whether to validate checkpoint integrity
        
        Returns:
            Checkpoint data dictionary or None if not found/invalid
        """
        if not self.checkpoint_file.exists():
            return None
        
        try:
            with open(self.checkpoint_file, "r", encoding="utf-8") as f:
                checkpoint = json.load(f)
            
            # Validate checkpoint
            if validate and not self._validate_checkpoint(checkpoint):
                print("Warning: Checkpoint integrity validation failed")
                return None
            
            return checkpoint
        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading checkpoint: {e}")
            return None
    
    def clear_checkpoint(self) -> bool:
        """
        Clear/delete checkpoint file.
        
        Returns:
            True if deleted successfully, False otherwise
        """
        try:
            if self.checkpoint_file.exists():
                self.checkpoint_file.unlink()
            return True
        except IOError as e:
            print(f"Error clearing checkpoint: {e}")
            return False
    
    def checkpoint_exists(self) -> bool:
        """
        Check if checkpoint file exists.
        
        Returns:
            True if checkpoint exists, False otherwise
        """
        return self.checkpoint_file.exists()
    
    def _calculate_integrity_hash(self, checkpoint: Dict[str, Any]) -> str:
        """
        Calculate integrity hash for checkpoint.
        
        Args:
            checkpoint: Checkpoint data dictionary
        
        Returns:
            SHA256 hash string
        """
        # Create a copy without the integrity_hash for hashing
        checkpoint_copy = checkpoint.copy()
        checkpoint_copy.pop("integrity_hash", None)
        checkpoint_copy.pop("last_updated", None)  # Exclude timestamp from hash
        
        # Convert to JSON string and hash
        json_str = json.dumps(checkpoint_copy, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(json_str.encode("utf-8")).hexdigest()
    
    def _validate_checkpoint(self, checkpoint: Dict[str, Any]) -> bool:
        """
        Validate checkpoint integrity.
        
        Args:
            checkpoint: Checkpoint data dictionary
        
        Returns:
            True if valid, False otherwise
        """
        # Check version
        if checkpoint.get("checkpoint_version") != self.CHECKPOINT_VERSION:
            print(f"Warning: Checkpoint version mismatch: {checkpoint.get('checkpoint_version')}")
            return False
        
        # Check required fields
        required_fields = [
            "started_at", "total_files", "processed_files",
            "processed_paths", "current_batch", "status"
        ]
        
        for field in required_fields:
            if field not in checkpoint:
                print(f"Warning: Missing required field in checkpoint: {field}")
                return False
        
        # Validate integrity hash
        stored_hash = checkpoint.get("integrity_hash")
        if stored_hash:
            calculated_hash = self._calculate_integrity_hash(checkpoint)
            if stored_hash != calculated_hash:
                print("Warning: Checkpoint integrity hash mismatch")
                return False
        
        # Validate data consistency
        processed_files = checkpoint.get("processed_files", 0)
        processed_paths = checkpoint.get("processed_paths", [])
        
        if processed_files != len(processed_paths):
            print(f"Warning: Processed files count mismatch: {processed_files} != {len(processed_paths)}")
            return False
        
        return True
    
    def get_checkpoint_progress(self) -> Optional[Dict[str, float]]:
        """
        Get checkpoint progress information.
        
        Returns:
            Dictionary with progress percentage and stats, or None if no checkpoint
        """
        checkpoint = self.load_checkpoint()
        if not checkpoint:
            return None
        
        total_files = checkpoint.get("total_files", 0)
        processed_files = checkpoint.get("processed_files", 0)
        
        if total_files == 0:
            progress_percent = 0.0
        else:
            progress_percent = (processed_files / total_files) * 100
        
        return {
            "progress_percent": progress_percent,
            "processed_files": processed_files,
            "total_files": total_files,
            "remaining_files": total_files - processed_files,
            "current_batch": checkpoint.get("current_batch", 0),
            "total_batches": checkpoint.get("total_batches", 0),
            "status": checkpoint.get("status", "unknown")
        }

