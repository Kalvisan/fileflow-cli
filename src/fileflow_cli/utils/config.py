"""Configuration management for FileFlowCLI."""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigManager:
    """Manages application configuration."""
    
    DEFAULT_CONFIG = {
        "language": "en",
        "llm_provider": "openai",
        "llm_model": "gpt-5.2",
        "llm_api_key": "",
        "batch_size": 100,
        "thread_count": 4
    }
    
    def __init__(self, working_directory: Optional[Path] = None):
        """
        Initialize configuration manager.
        
        Args:
            working_directory: Working directory path (default: current directory)
        """
        if working_directory is None:
            working_directory = Path.cwd()
        
        self.working_directory = Path(working_directory).resolve()
        self.config_dir = self._find_or_create_config_dir()
        self.config_file = self.config_dir / "config.json"
        self.config: Dict[str, Any] = {}
        self._load_config()
    
    def _find_or_create_config_dir(self) -> Path:
        """
        Find or create .fileflow_cli directory.
        
        Returns:
            Path to .fileflow_cli directory
        """
        config_dir = self.working_directory / ".fileflow_cli"
        
        # Check if .fileflow_cli exists in current directory
        if config_dir.exists():
            return config_dir
        
        # Check parent directories for existing .fileflow_cli
        parent_config = self._find_parent_fileflow_cli()
        if parent_config:
            return parent_config
        
        # Create new .fileflow_cli directory
        config_dir.mkdir(exist_ok=True)
        return config_dir
    
    def _find_parent_fileflow_cli(self) -> Optional[Path]:
        """
        Walk up directory tree looking for .fileflow_cli directory.
        
        Returns:
            Path to .fileflow_cli if found, None otherwise
        """
        current = self.working_directory.parent
        
        while current != current.parent:  # Stop at filesystem root
            config_dir = current / ".fileflow_cli"
            if config_dir.exists() and config_dir.is_dir():
                return config_dir
            current = current.parent
        
        return None
    
    def _load_config(self) -> None:
        """Load configuration from file or create default."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    self.config = json.load(f)
                
                # Merge with defaults to ensure all keys exist
                for key, value in self.DEFAULT_CONFIG.items():
                    if key not in self.config:
                        self.config[key] = value
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Warning: Could not load config: {e}")
                self.config = self.DEFAULT_CONFIG.copy()
                self._save_config()
        else:
            self.config = self.DEFAULT_CONFIG.copy()
            self._save_config()
    
    def _save_config(self) -> None:
        """Save configuration to file."""
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Warning: Could not save config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
        
        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value
        self._save_config()
    
    def get_config_dir(self) -> Path:
        """
        Get configuration directory path.
        
        Returns:
            Path to .fileflow_cli directory
        """
        return self.config_dir
    
    def get_config_file(self) -> Path:
        """
        Get configuration file path.
        
        Returns:
            Path to config.json
        """
        return self.config_file


# Global config manager instance
_config_manager: Optional[ConfigManager] = None


def init_config(working_directory: Optional[Path] = None) -> ConfigManager:
    """
    Initialize global configuration manager.
    
    Args:
        working_directory: Working directory path (default: current directory)
    
    Returns:
        ConfigManager instance
    """
    global _config_manager
    _config_manager = ConfigManager(working_directory)
    return _config_manager


def get_config(key: str = None, default: Any = None) -> Any:
    """
    Get configuration value (convenience function).
    
    Args:
        key: Configuration key (if None, returns full config dict)
        default: Default value if key not found
    
    Returns:
        Configuration value or full config dict if key is None
    """
    global _config_manager
    
    if _config_manager is None:
        init_config()
    
    if key is None:
        return _config_manager.config
    
    return _config_manager.get(key, default)


def set_config(key: str, value: Any) -> None:
    """
    Set configuration value (convenience function).
    
    Args:
        key: Configuration key
        value: Configuration value
    """
    global _config_manager
    
    if _config_manager is None:
        init_config()
    
    _config_manager.set(key, value)

