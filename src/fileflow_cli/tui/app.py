"""Main TUI application for FileFlowCLI."""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Label
from textual.binding import Binding

from ..i18n.translations import init_translations, t
from ..utils.config import init_config, get_config
from ..storage.index_storage import IndexStorage
from ..storage.checkpoint_manager import CheckpointManager
from .screens.indexing import IndexingScreen
from pathlib import Path


class FileFlowCLIApp(App):
    """Main application class for FileFlowCLI TUI."""
    
    CSS = """
    Screen {
        background: $surface;
    }
    
    #menu_bar {
        height: 3;
        border-bottom: solid $primary;
        background: $panel;
    }
    
    #menu_bar Horizontal {
        height: 100%;
        align: center middle;
    }
    
    .menu_item {
        padding: 0 2;
        text-style: bold;
        color: $text;
    }
    
    .menu_item:hover {
        background: $primary;
        color: $text;
    }
    
    #content_area {
        height: 1fr;
        padding: 1;
    }
    
    #status_bar {
        height: 3;
        border-top: solid $primary;
        background: $panel;
    }
    
    #status_bar Horizontal {
        height: 100%;
        align: center middle;
    }
    
    .status_item {
        padding: 0 2;
        color: $text-muted;
    }
    
    #main_content {
        width: 100%;
        height: 100%;
        padding: 1;
    }
    
    .section_title {
        text-style: bold;
        color: $primary;
        margin-bottom: 1;
    }
    
    .info_text {
        color: $text;
        margin: 1 0;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("i", "start_indexing", "Indexing", priority=True),
        Binding("v", "view_files", "View Files", priority=True),
        Binding("a", "analyze_llm", "Analyze", priority=True),
        Binding("s", "settings", "Settings", priority=True),
        Binding("h", "help", "Help", priority=True),
    ]
    
    def __init__(self):
        """Initialize the application."""
        super().__init__()
        # Initialize translations
        language = get_config("language", "en")
        init_translations(language)
        # Initialize config
        config_manager = init_config()
        self.config_dir = config_manager.get_config_dir()
        self.working_directory = config_manager.working_directory
        self.index_storage = IndexStorage(self.config_dir)
        self.checkpoint_manager = CheckpointManager(self.config_dir)
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        # Menu bar at top
        with Container(id="menu_bar"):
            with Horizontal():
                yield Static(f"[i] {t('main_menu.start_indexing')}", classes="menu_item")
                yield Static(f"[v] {t('main_menu.view_files')}", classes="menu_item")
                yield Static(f"[a] {t('main_menu.analyze_llm')}", classes="menu_item")
                yield Static(f"[s] {t('main_menu.settings')}", classes="menu_item")
                yield Static(f"[q] {t('main_menu.exit')}", classes="menu_item")
        
        # Main content area
        with Container(id="content_area"):
            yield Static(id="main_content")
        
        # Status bar at bottom
        with Container(id="status_bar"):
            with Horizontal():
                yield Static(id="status_indexing")
                yield Static("|", classes="status_item")
                yield Static(id="status_files")
                yield Static("|", classes="status_item")
                yield Static(id="status_language")
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when app is mounted."""
        self.title = t("app.title")
        self.sub_title = t("app.subtitle")
        self._update_status_bar()
        self._update_main_content()
    
    def _update_status_bar(self) -> None:
        """Update status bar information."""
        # Check indexing status
        indexed_at = self.index_storage.get_indexed_at()
        checkpoint_exists = self.checkpoint_manager.checkpoint_exists()
        
        if checkpoint_exists:
            status_text = f"{t('status.indexing')}: {t('indexing.in_progress')} (checkpoint)"
        elif indexed_at:
            status_text = f"{t('status.indexing')}: {t('indexing.complete')}"
        else:
            status_text = f"{t('status.indexing')}: {t('indexing.not_started')}"
        
        self.query_one("#status_indexing", Static).update(status_text)
        
        # File count
        file_count = self.index_storage.get_file_count()
        files_text = f"{t('status.files_indexed')}: {file_count}"
        self.query_one("#status_files", Static).update(files_text)
        
        # Language
        lang = get_config("language", "en")
        lang_text = f"{t('status.language')}: {lang.upper()}"
        self.query_one("#status_language", Static).update(lang_text)
    
    def _update_main_content(self) -> None:
        """Update main content area."""
        indexed_at = self.index_storage.get_indexed_at()
        file_count = self.index_storage.get_file_count()
        checkpoint_exists = self.checkpoint_manager.checkpoint_exists()
        
        if checkpoint_exists:
            # Checkpoint exists - offer to resume
            progress = self.checkpoint_manager.get_checkpoint_progress()
            if progress:
                content = (
                    f"{t('content.welcome')}\n\n"
                    f"Indexing checkpoint found!\n\n"
                    f"Progress: {progress['progress_percent']:.1f}%\n"
                    f"Processed: {progress['processed_files']}/{progress['total_files']} files\n\n"
                    f"Press [i] to resume indexing or [c] to cancel and start fresh."
                )
            else:
                content = (
                    f"{t('content.welcome')}\n\n"
                    f"Indexing checkpoint found!\n\n"
                    f"Press [i] to resume indexing."
                )
        elif indexed_at:
            content = (
                f"{t('content.welcome')}\n\n"
                f"{t('content.instructions')}\n\n"
                f"• {t('indexing.complete')}\n"
                f"• {t('indexing.last_indexed', timestamp=indexed_at[:19])}\n"
                f"• {file_count} {t('status.files_indexed').lower()}\n\n"
                f"Press [i] to re-index or [v] to view files."
            )
        else:
            content = (
                f"{t('content.welcome')}\n\n"
                f"{t('content.instructions')}\n\n"
                f"{t('content.no_files')}\n\n"
                f"Press [i] to start indexing."
            )
        
        self.query_one("#main_content", Static).update(content)
    
    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()
    
    def action_start_indexing(self) -> None:
        """Start indexing action."""
        # Push indexing screen
        indexing_screen = IndexingScreen(
            str(self.working_directory),
            self.config_dir
        )
        self.push_screen(indexing_screen)
    
    def action_view_files(self) -> None:
        """View indexed files."""
        file_count = self.index_storage.get_file_count()
        if file_count > 0:
            self.query_one("#main_content", Static).update(
                f"{t('main_menu.view_files')}\n\n"
                f"File table will be displayed here.\n"
                f"Currently indexed: {file_count} files."
            )
        else:
            self.query_one("#main_content", Static).update(
                f"{t('main_menu.view_files')}\n\n"
                f"{t('content.no_files')}\n"
                f"Press [i] to start indexing first."
            )
    
    def action_analyze_llm(self) -> None:
        """Analyze with LLM."""
        file_count = self.index_storage.get_file_count()
        if file_count > 0:
            self.query_one("#main_content", Static).update(
                f"{t('main_menu.analyze_llm')}\n\n"
                f"LLM analysis functionality will be implemented later.\n"
                f"Currently indexed: {file_count} files."
            )
        else:
            self.query_one("#main_content", Static).update(
                f"{t('main_menu.analyze_llm')}\n\n"
                f"{t('content.no_files')}\n"
                f"Press [i] to start indexing first."
            )
    
    def action_settings(self) -> None:
        """Open settings."""
        content = (
            f"{t('settings.title')}\n\n"
            f"{t('settings.language')}: {get_config('language', 'en')}\n"
            f"{t('settings.llm_provider')}: {get_config('llm_provider', 'openai')}\n"
            f"{t('settings.thread_count')}: {get_config('thread_count', 4)}\n"
            f"{t('settings.batch_size')}: {get_config('batch_size', 100)}\n\n"
            f"Settings editing will be implemented later."
        )
        self.query_one("#main_content", Static).update(content)
    
    def action_help(self) -> None:
        """Show help information."""
        content = (
            f"{t('app.title')} - {t('shortcuts.help')}\n\n"
            f"Keyboard Shortcuts:\n"
            f"  [i] - {t('main_menu.start_indexing')}\n"
            f"  [v] - {t('main_menu.view_files')}\n"
            f"  [a] - {t('main_menu.analyze_llm')}\n"
            f"  [s] - {t('main_menu.settings')}\n"
            f"  [h] - {t('shortcuts.help')}\n"
            f"  [q] - {t('shortcuts.quit')}\n\n"
            f"Features:\n"
            f"  • File indexing with checkpoint support\n"
            f"  • LLM-powered file organization\n"
            f"  • Version control with rollback\n"
            f"  • Multi-language support"
        )
        self.query_one("#main_content", Static).update(content)

