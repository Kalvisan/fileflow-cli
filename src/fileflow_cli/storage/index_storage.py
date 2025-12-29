"""Index storage system for FileFlowCLI."""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime


class IndexStorage:
    """Manages index storage for FileFlowCLI."""
    
    INDEX_FILENAME = "index.json"
    
    def __init__(self, config_dir: Path):
        """
        Initialize index storage.
        
        Args:
            config_dir: Path to .fileflow_cli directory
        """
        self.config_dir = Path(config_dir)
        self.index_file = self.config_dir / self.INDEX_FILENAME
    
    def save_index(self, index_data: List[Dict[str, Any]]) -> bool:
        """
        Save index to disk.
        
        Args:
            index_data: List of file metadata dictionaries
        
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            # Ensure config directory exists
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
            # Prepare index structure
            index = {
                "indexed_at": datetime.now().isoformat(),
                "file_count": len(index_data),
                "files": index_data
            }
            
            # Save to file
            with open(self.index_file, "w", encoding="utf-8") as f:
                json.dump(index, f, indent=2, ensure_ascii=False)
            
            return True
        
        except (IOError, json.JSONEncodeError) as e:
            print(f"Error saving index: {e}")
            return False
    
    def load_index(self) -> Optional[Dict[str, Any]]:
        """
        Load index from disk.
        
        Returns:
            Index data dictionary or None if not found
        """
        if not self.index_file.exists():
            return None
        
        try:
            with open(self.index_file, "r", encoding="utf-8") as f:
                index = json.load(f)
            
            return index
        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading index: {e}")
            return None
    
    def index_exists(self) -> bool:
        """
        Check if index file exists.
        
        Returns:
            True if index exists, False otherwise
        """
        return self.index_file.exists()
    
    def get_indexed_at(self) -> Optional[str]:
        """
        Get timestamp of when index was last created.
        
        Returns:
            ISO timestamp string or None if no index
        """
        index = self.load_index()
        if index:
            return index.get("indexed_at")
        return None
    
    def get_file_count(self) -> int:
        """
        Get number of files in index.
        
        Returns:
            Number of files or 0 if no index
        """
        index = self.load_index()
        if index:
            return index.get("file_count", 0)
        return 0

