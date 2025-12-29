"""Translation system for FileFlowCLI."""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class TranslationManager:
    """Manages translations for the application."""
    
    def __init__(self, language: str = "en"):
        """
        Initialize translation manager.
        
        Args:
            language: Language code (default: "en")
        """
        self.language = language
        self.translations: Dict[str, Any] = {}
        self._load_translations()
    
    def _load_translations(self) -> None:
        """Load translations from JSON file."""
        # Get the directory where this file is located
        i18n_dir = Path(__file__).parent
        translation_file = i18n_dir / f"{self.language}.json"
        
        if not translation_file.exists():
            # Fallback to English if language file doesn't exist
            translation_file = i18n_dir / "en.json"
        
        try:
            with open(translation_file, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # If loading fails, use empty translations
            self.translations = {}
            print(f"Warning: Could not load translations: {e}")
    
    def get(self, key: str, **kwargs) -> str:
        """
        Get translation for a key.
        
        Args:
            key: Translation key (e.g., "main_menu.start_indexing")
            **kwargs: Format arguments for the translation string
        
        Returns:
            Translated string with formatted arguments
        """
        keys = key.split(".")
        value = self.translations
        
        try:
            for k in keys:
                value = value[k]
            
            # If value is a string, format it with kwargs
            if isinstance(value, str):
                return value.format(**kwargs) if kwargs else value
            return str(value)
        except (KeyError, TypeError):
            # Return the key itself if translation not found
            return key
    
    def set_language(self, language: str) -> None:
        """
        Change the language.
        
        Args:
            language: Language code (e.g., "en", "lv", "ru")
        """
        self.language = language
        self._load_translations()


# Global translation manager instance
_translation_manager: Optional[TranslationManager] = None


def init_translations(language: str = "en") -> None:
    """
    Initialize the global translation manager.
    
    Args:
        language: Language code (default: "en")
    """
    global _translation_manager
    _translation_manager = TranslationManager(language)


def t(key: str, **kwargs) -> str:
    """
    Get translation for a key (convenience function).
    
    Args:
        key: Translation key (e.g., "main_menu.start_indexing")
        **kwargs: Format arguments for the translation string
    
    Returns:
        Translated string with formatted arguments
    
    Example:
        >>> t("main_menu.start_indexing")
        "Start Indexing"
        >>> t("errors.file_not_found", path="/tmp/file.txt")
        "File not found: /tmp/file.txt"
    """
    global _translation_manager
    
    if _translation_manager is None:
        # Initialize with default language if not initialized
        init_translations()
    
    return _translation_manager.get(key, **kwargs)


def set_language(language: str) -> None:
    """
    Change the global language.
    
    Args:
        language: Language code (e.g., "en", "lv", "ru")
    """
    global _translation_manager
    
    if _translation_manager is None:
        init_translations(language)
    else:
        _translation_manager.set_language(language)

