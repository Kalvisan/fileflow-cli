"""Dynamic error handling system for FileFlowCLI."""

import traceback
import sys
from typing import Dict, Any, Optional, Type
from enum import Enum
from datetime import datetime


class ErrorType(Enum):
    """Error type enumeration."""
    FILE_OPERATION = "file_operation"
    LLM = "llm"
    INDEXING = "indexing"
    CONFIG = "config"
    UNKNOWN = "unknown"


class FileOperationError(Exception):
    """Error related to file operations."""
    pass


class LLMError(Exception):
    """Error related to LLM operations."""
    pass


class IndexingError(Exception):
    """Error related to indexing operations."""
    pass


class ConfigError(Exception):
    """Error related to configuration operations."""
    pass


class ErrorHandler:
    """Centralized error handling system."""
    
    def __init__(self):
        """Initialize error handler."""
        self.error_log: list = []
        self.show_details = False
    
    def handle_error(
        self,
        error: Exception,
        context: Optional[Dict[str, Any]] = None,
        error_type: Optional[ErrorType] = None
    ) -> str:
        """
        Handle an error and return user-friendly message.
        
        Args:
            error: Exception that occurred
            context: Additional context information
            error_type: Type of error (auto-detected if None)
        
        Returns:
            User-friendly error message
        """
        if context is None:
            context = {}
        
        if error_type is None:
            error_type = self._detect_error_type(error)
        
        # Get detailed error information
        error_info = self._get_error_info(error, context, error_type)
        
        # Store error for debugging
        self.error_log.append(error_info)
        
        # Generate user-friendly message
        user_message = self._generate_user_message(error, error_type, context)
        
        # Log detailed error for developer
        self._log_error_details(error_info)
        
        return user_message
    
    def _detect_error_type(self, error: Exception) -> ErrorType:
        """
        Detect error type from exception.
        
        Args:
            error: Exception instance
        
        Returns:
            ErrorType enum value
        """
        if isinstance(error, FileOperationError):
            return ErrorType.FILE_OPERATION
        elif isinstance(error, LLMError):
            return ErrorType.LLM
        elif isinstance(error, IndexingError):
            return ErrorType.INDEXING
        elif isinstance(error, ConfigError):
            return ErrorType.CONFIG
        else:
            return ErrorType.UNKNOWN
    
    def _get_error_info(
        self,
        error: Exception,
        context: Dict[str, Any],
        error_type: ErrorType
    ) -> Dict[str, Any]:
        """
        Get detailed error information.
        
        Args:
            error: Exception instance
            context: Additional context
            error_type: Type of error
        
        Returns:
            Dictionary with error details
        """
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Get file and line number from traceback
        file_path = "unknown"
        line_number = 0
        
        if exc_traceback:
            tb_frame = exc_traceback.tb_frame
            if tb_frame:
                file_path = tb_frame.f_code.co_filename
                line_number = exc_traceback.tb_lineno
        
        # Get stack trace
        stack_trace = traceback.format_exc()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "error_type": error_type.value,
            "exception_type": type(error).__name__,
            "message": str(error),
            "file": file_path,
            "line": line_number,
            "stack_trace": stack_trace,
            "context": context
        }
    
    def _generate_user_message(
        self,
        error: Exception,
        error_type: ErrorType,
        context: Dict[str, Any]
    ) -> str:
        """
        Generate user-friendly error message.
        
        Args:
            error: Exception instance
            error_type: Type of error
            context: Additional context
        
        Returns:
            User-friendly message
        """
        error_msg = str(error)
        
        if error_type == ErrorType.FILE_OPERATION:
            path = context.get("path", context.get("file_path", "unknown"))
            operation = context.get("operation", "operation")
            
            if "not found" in error_msg.lower() or FileNotFoundError in type(error).__mro__:
                return f"File not found: {path}. Please check the file path."
            elif "permission" in error_msg.lower() or PermissionError in type(error).__mro__:
                return f"Permission denied: {path}. Please check file permissions."
            else:
                return f"File operation failed: {error_msg}"
        
        elif error_type == ErrorType.LLM:
            if "api" in error_msg.lower() or "key" in error_msg.lower():
                return f"LLM API error: Please check your API key and configuration."
            elif "network" in error_msg.lower() or "connection" in error_msg.lower():
                return f"Network error: Could not connect to LLM service. Please check your internet connection."
            else:
                return f"LLM error: {error_msg}"
        
        elif error_type == ErrorType.INDEXING:
            return f"Indexing error: {error_msg}"
        
        elif error_type == ErrorType.CONFIG:
            return f"Configuration error: {error_msg}"
        
        else:
            return f"An error occurred: {error_msg}"
    
    def _log_error_details(self, error_info: Dict[str, Any]) -> None:
        """
        Log detailed error information for developer.
        
        Args:
            error_info: Error information dictionary
        """
        # In production, this would write to a log file
        # For now, we'll just store it in memory
        pass
    
    def get_error_details(self, index: int = -1) -> Optional[Dict[str, Any]]:
        """
        Get detailed error information.
        
        Args:
            index: Error index (-1 for latest)
        
        Returns:
            Error details dictionary or None
        """
        if not self.error_log:
            return None
        
        try:
            return self.error_log[index]
        except IndexError:
            return None
    
    def format_error_details(self, error_info: Dict[str, Any]) -> str:
        """
        Format error details for display.
        
        Args:
            error_info: Error information dictionary
        
        Returns:
            Formatted error details string
        """
        lines = [
            f"Error Type: {error_info['error_type']}",
            f"Exception: {error_info['exception_type']}",
            f"Message: {error_info['message']}",
            f"File: {error_info['file']}",
            f"Line: {error_info['line']}",
            f"Timestamp: {error_info['timestamp']}",
        ]
        
        if error_info.get('context'):
            lines.append(f"Context: {error_info['context']}")
        
        lines.append("\nStack Trace:")
        lines.append(error_info['stack_trace'])
        
        return "\n".join(lines)
    
    def toggle_details(self) -> None:
        """Toggle showing detailed error information."""
        self.show_details = not self.show_details


# Global error handler instance
_error_handler: Optional[ErrorHandler] = None


def init_error_handler() -> ErrorHandler:
    """
    Initialize global error handler.
    
    Returns:
        ErrorHandler instance
    """
    global _error_handler
    _error_handler = ErrorHandler()
    return _error_handler


def handle_error(
    error: Exception,
    context: Optional[Dict[str, Any]] = None,
    error_type: Optional[ErrorType] = None
) -> str:
    """
    Handle an error (convenience function).
    
    Args:
        error: Exception that occurred
        context: Additional context information
        error_type: Type of error (auto-detected if None)
    
    Returns:
        User-friendly error message
    """
    global _error_handler
    
    if _error_handler is None:
        init_error_handler()
    
    return _error_handler.handle_error(error, context, error_type)

