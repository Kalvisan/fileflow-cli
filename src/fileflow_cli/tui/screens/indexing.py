"""Indexing screen for FileFlowCLI."""

import threading
from pathlib import Path
from textual.app import ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Static, ProgressBar, DataTable, Footer
from collections import deque
from textual.screen import Screen
from textual.binding import Binding

from ...i18n.translations import t
from ...core.indexer import FileIndexer
from ...storage.checkpoint_manager import CheckpointManager
from ...storage.index_storage import IndexStorage


class IndexingScreen(Screen):
    """Screen for displaying indexing progress."""
    
    BINDINGS = [
        Binding("p", "pause", "Pause", priority=True),
        Binding("r", "resume", "Resume", priority=True),
        Binding("c", "cancel", "Cancel", priority=True),
        Binding("/", "search", "Search", priority=True),
        Binding("q", "quit", "Quit", priority=True),
    ]
    
    CSS = """
    #indexing_container {
        padding: 1;
    }
    
    #progress_section {
        height: 6;
        border: solid $primary;
        padding: 1;
    }
    
    #file_table_section {
        height: 1fr;
        border: solid $primary;
        padding: 1;
    }
    
    .progress_label {
        text-style: bold;
        color: $primary;
    }
    
    .stats_text {
        color: $text-muted;
    }
    
    #file_table {
        height: 100%;
    }
    """
    
    def __init__(self, directory: str, config_dir):
        """
        Initialize indexing screen.
        
        Args:
            directory: Directory to index
            config_dir: Configuration directory path
        """
        super().__init__()
        self.directory = Path(directory)
        self.config_dir = config_dir
        self.indexer = FileIndexer(config_dir)
        self.checkpoint_manager = CheckpointManager(config_dir)
        self.index_storage = IndexStorage(config_dir)
        self.is_paused = False
        self.is_cancelled = False
        self.indexing_thread = None
        self.indexed_files = []
        self.recent_files = deque(maxlen=50)  # Keep last 50 processed files
        self.current_processing = []  # Files currently being processed
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the indexing screen."""
        with Container(id="indexing_container"):
            # Progress section (top)
            with Vertical(id="progress_section"):
                yield Static(t("main_menu.start_indexing"), classes="progress_label")
                yield ProgressBar(total=100, id="progress_bar")
                with Horizontal():
                    yield Static(id="progress_stats")
                    yield Static(id="progress_speed")
                yield Static(id="progress_status")
            
            # File processing table (bottom)
            with Container(id="file_table_section"):
                yield Static("Recent files:", classes="progress_label")
                yield DataTable(id="file_table", zebra_stripes=True)
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when screen is mounted."""
        self.title = t("main_menu.start_indexing")
        # Setup file table
        file_table = self.query_one("#file_table", DataTable)
        file_table.add_columns("Status", "File", "Size", "Type")
        file_table.cursor_type = "row"
        self._start_indexing()
    
    def _start_indexing(self) -> None:
        """Start or resume indexing in background thread."""
        self.is_paused = False
        self.is_cancelled = False
        
        # Check if checkpoint exists
        checkpoint = self.checkpoint_manager.load_checkpoint()
        
        if checkpoint:
            self._update_status(t("indexing.resuming"))
        else:
            self._update_status(t("indexing.starting"))
        
        # Start indexing in background thread
        self.indexing_thread = threading.Thread(
            target=self._run_indexing,
            daemon=True
        )
        self.indexing_thread.start()
    
    def _run_indexing(self) -> None:
        """Run indexing in background thread."""
        try:
            checkpoint = self.checkpoint_manager.load_checkpoint()
            
            if checkpoint:
                progress_iterator = self.indexer.resume_indexing(self.directory)
            else:
                progress_iterator = self.indexer.index_directory(self.directory)
            
            indexed_files = []
            
            for progress_update in progress_iterator:
                if self.is_cancelled:
                    break
                
                while self.is_paused and not self.is_cancelled:
                    self.call_from_thread(self._update_status, t("indexing.paused"))
                    threading.Event().wait(0.5)
                
                if self.is_cancelled:
                    break
                
                # Update progress with file information
                recent_files = progress_update.get("recent_files", [])
                if recent_files:
                    self.call_from_thread(self._update_file_list, recent_files)
                else:
                    # Fallback to checkpoint data
                    checkpoint_data = self.checkpoint_manager.load_checkpoint()
                    if checkpoint_data:
                        processed_paths = checkpoint_data.get("processed_paths", [])
                        if processed_paths:
                            recent = processed_paths[-10:]  # Last 10 files
                            self.call_from_thread(self._update_file_list, recent)
                
                # Update progress
                self.call_from_thread(self._update_progress, progress_update)
                
                # Collect files if complete
                if progress_update.get("complete"):
                    # Load final index from checkpoint
                    final_checkpoint = self.checkpoint_manager.load_checkpoint()
                    if final_checkpoint:
                        file_hashes = final_checkpoint.get("file_hashes", {})
                        # We'll need to rebuild full file list
                        # For now, mark as complete
                        pass
            
            if not self.is_cancelled:
                # Save index (simplified for now)
                # Full implementation will save complete file metadata
                self.call_from_thread(self._update_status, t("indexing.complete_msg"))
                self.call_from_thread(self.set_timer, 2.0, self._return_to_main)
        
        except Exception as e:
            self.call_from_thread(self._update_status, f"Error: {str(e)}")
    
    def _update_progress(self, progress: dict) -> None:
        """Update progress display."""
        total_files = progress.get("total_files", 0)
        processed_files = progress.get("processed_files", 0)
        current_batch = progress.get("current_batch", 0)
        total_batches = progress.get("total_batches", 0)
        progress_percent = progress.get("progress_percent", 0.0)
        
        # Update progress bar
        progress_bar = self.query_one("#progress_bar", ProgressBar)
        progress_bar.update(progress=progress_percent)
        
        # Update stats
        stats_text = t(
            "indexing.files_stats",
            processed=processed_files,
            total=total_files,
            batch=current_batch,
            total_batches=total_batches
        )
        self.query_one("#progress_stats", Static).update(stats_text)
        
        # Update status
        status_text = t("indexing.processing", percent=f"{progress_percent:.1f}")
        self._update_status(status_text)
    
    def _update_status(self, message: str) -> None:
        """Update status message."""
        self.query_one("#progress_status", Static).update(message)
    
    def _update_file_list(self, file_paths: list) -> None:
        """Update file list with recently processed files."""
        file_table = self.query_one("#file_table", DataTable)
        
        # Add new files to the list (don't clear, just append)
        for file_path in file_paths:
            # Check if file already in table
            file_path_str = str(file_path)[:60]
            already_added = False
            
            for row_key in file_table.rows:
                row_data = file_table.get_row(row_key)
                if len(row_data) > 1 and row_data[1] == file_path_str:
                    # Update status to completed
                    file_table.update_cell(row_key, "Status", "✓")
                    already_added = True
                    break
            
            if not already_added:
                try:
                    file_obj = self.directory / file_path
                    if file_obj.exists():
                        size = file_obj.stat().st_size
                        size_str = self._format_size(size)
                        file_type = file_obj.suffix or "file"
                        
                        file_table.add_row(
                            "✓",  # Status
                            file_path_str,  # File path (truncated)
                            size_str,  # Size
                            file_type  # Type
                        )
                    else:
                        file_table.add_row(
                            "✓",
                            file_path_str,
                            "?",
                            "?"
                        )
                except Exception:
                    # Skip files that can't be accessed
                    file_table.add_row(
                        "✓",
                        file_path_str,
                        "?",
                        "?"
                    )
        
        # Keep only last 50 rows
        while file_table.row_count > 50:
            file_table.remove_row(file_table.rows[0])
        
        # Scroll to top to show newest files
        if file_table.row_count > 0:
            file_table.cursor_row = 0
    
    def action_pause(self) -> None:
        """Pause indexing."""
        if not self.is_paused:
            self.is_paused = True
            self._update_status(t("indexing.paused"))
    
    def action_resume(self) -> None:
        """Resume indexing."""
        if self.is_paused:
            self.is_paused = False
            self._update_status("Resuming...")
    
    def action_cancel(self) -> None:
        """Cancel indexing."""
        self.is_cancelled = True
        self._update_status(t("indexing.cancelled"))
        self.set_timer(1.0, self._return_to_main)
    
    def action_search(self) -> None:
        """Open search dialog."""
        # Search functionality will be implemented in Step 14
        self._update_status("Search functionality coming soon...")
    
    def action_quit(self) -> None:
        """Quit application."""
        self.is_cancelled = True
        self.app.exit()
    
    def _return_to_main(self) -> None:
        """Return to main screen."""
        self.app.pop_screen()
        # Refresh main screen
        if hasattr(self.app, "_update_status_bar"):
            self.app._update_status_bar()
        if hasattr(self.app, "_update_main_content"):
            self.app._update_main_content()
    
    def _format_size(self, size: int) -> str:
        """Format file size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} PB"
