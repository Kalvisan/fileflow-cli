---
name: File Sorter TUI System
overview: Create a Python TUI tool with Textual library that helps organize files and directories using LLM analysis, with version control system and multi-language support.
todos:
  - id: setup_project
    content: Create project structure, requirements.txt, and .gitignore
    status: pending
  - id: i18n_system
    content: Implement translation system with JSON files (lv, ru, en) - English by default, dynamic language switching from main menu
    status: pending
    dependencies:
      - setup_project
  - id: config_system
    content: Create configuration system (.file_sorter/config.json) with LLM settings
    status: pending
    dependencies:
      - setup_project
  - id: checkpoint_manager
    content: Implement checkpoint management (storage/checkpoint_manager.py) - checkpoint saving, resuming, hash verification
    status: pending
    dependencies:
      - setup_project
  - id: indexer
    content: Implement efficient file indexing with recursive directory traversal, batch processing, parallel processing and checkpoint integration (10000+ files support)
    status: pending
    dependencies:
      - setup_project
      - checkpoint_manager
  - id: analyzer
    content: Create efficient surface-level file analysis (magic numbers, metadata, previews only, not full files) with parallel processing
    status: pending
    dependencies:
      - indexer
  - id: version_manager
    content: Implement version management with JSON storage and rollback functionality
    status: pending
    dependencies:
      - setup_project
  - id: llm_client
    content: Create LLM client with support for multiple providers (OpenAI, Anthropic, Ollama) with privacy control - user chooses what to send, private files are not sent
    status: pending
    dependencies:
      - config_system
  - id: file_operations
    content: Implement file operations (move, rename, directory creation) with validation
    status: pending
    dependencies:
      - version_manager
  - id: tui_base
    content: Create Textual base application with screen navigation
    status: pending
    dependencies:
      - i18n_system
  - id: indexing_status_check
    content: Implement indexing status check on TUI launch - check last indexing time, block functions if indexing not done, show status in header
    status: pending
    dependencies:
      - indexer
      - tui_base
  - id: main_screen
    content: Create main screen (tui/screens/main_screen.py) with top-like UI - header with stats, file table below, function blocking when indexing not done
    status: pending
    dependencies:
      - tui_base
      - indexing_status_check
  - id: indexing_screen_realtime
    content: Create indexing screen (tui/screens/indexing.py) with top-like UI - real-time status header, live file processing table, updates every 100-500ms
    status: pending
    dependencies:
      - tui_base
      - indexer
      - checkpoint_manager
  - id: file_table_widget
    content: Create file table widget (tui/widgets/file_table.py) - sortable, filterable table with real-time updates, pagination for large file counts
    status: pending
    dependencies:
      - tui_base
      - indexer
  - id: status_header_widget
    content: Create status header widget (tui/widgets/status_header.py) - top section with indexing status, system stats, quick actions
    status: pending
    dependencies:
      - tui_base
      - indexing_status_check
  - id: tui_screens
    content: Implement all TUI screens (main screen with top-like UI, language selection, indexing screen with real-time status, analysis, preview, rollback, privacy, help, settings) with private file marking functionality and function blocking
    status: pending
    dependencies:
      - main_screen
      - indexing_screen_realtime
      - file_table_widget
      - status_header_widget
      - tui_base
      - analyzer
      - llm_client
      - file_operations
  - id: help_screen
    content: Create help screen (tui/screens/help.py) with detailed guide, FAQ, keyboard shortcuts and multi-language support
    status: pending
    dependencies:
      - i18n_system
      - tui_base
  - id: privacy_manager
    content: Implement private file management (core/privacy_manager.py) - marking after indexing, global exceptions (directories/files/extensions), storing in exceptions.json, filtering in LLM analysis, showing ignored files in table
    status: pending
    dependencies:
      - indexer
  - id: exceptions_system
    content: Implement exceptions system - mark directories/files/extensions to ignore, store in exceptions.json, display ignored files in separate table section, persist across sessions
    status: pending
    dependencies:
      - privacy_manager
      - indexer
  - id: privacy_features
    content: Implement privacy features UI - private file/directory marking on screen, LLM data sending control with warnings before sending
    status: pending
    dependencies:
      - privacy_manager
      - llm_client
      - tui_screens
  - id: main_integration
    content: Integrate all components in main application and test full workflow
    status: pending
    dependencies:
      - tui_screens
  - id: pip_package
    content: Create setup.py and pyproject.toml for pip package with entry point 'file-sorter'
    status: pending
    dependencies:
      - setup_project
  - id: python_checker
    content: Implement Python version check (scripts/check_python.py) with multi-language error messages
    status: pending
    dependencies:
      - i18n_system
  - id: install_guide
    content: Create installation instruction system (scripts/install_guide.py) for all OS with multi-language support
    status: pending
    dependencies:
      - i18n_system
  - id: install_scripts
    content: Create installation scripts (install.sh, install.bat, install.ps1) with Python check and automated installation
    status: pending
    dependencies:
      - pip_package
      - python_checker
      - install_guide
  - id: error_handling
    content: Implement comprehensive error handling system - graceful error recovery, user-friendly error messages, error logging, transaction rollback on failures
    status: pending
    dependencies:
      - file_operations
      - version_manager
  - id: logging_system
    content: Implement logging system (utils/logger.py) - structured logging, log levels, log rotation, debug mode, error tracking
    status: pending
    dependencies:
      - setup_project
  - id: atomic_operations
    content: Implement atomic file operations - transaction-like behavior, rollback on partial failures, file operation validation before execution
    status: pending
    dependencies:
      - file_operations
      - version_manager
  - id: config_validation
    content: Implement configuration validation - schema validation, default values, migration from old configs, validation error messages
    status: pending
    dependencies:
      - config_system
  - id: keyboard_shortcuts
    content: Implement keyboard shortcuts system - global shortcuts, context-aware shortcuts, customizable shortcuts, help display
    status: pending
    dependencies:
      - tui_base
      - help_screen
  - id: testing_framework
    content: Set up testing framework - unit tests, integration tests, TUI testing, mock LLM responses, test fixtures
    status: pending
    dependencies:
      - setup_project
  - id: ci_cd_pipeline
    content: Create CI/CD pipeline - GitHub Actions for testing, security scanning, code quality checks, automated releases
    status: pending
    dependencies:
      - testing_framework
      - pip_package
  - id: code_quality
    content: Set up code quality tools - black for formatting, ruff for linting, mypy for type checking, pre-commit hooks
    status: pending
    dependencies:
      - setup_project
  - id: documentation
    content: Create documentation structure - API documentation, user guide, developer guide, architecture documentation
    status: pending
    dependencies:
      - main_integration
  - id: performance_monitoring
    content: Implement performance monitoring - operation timing, memory usage tracking, performance metrics display in UI
    status: pending
    dependencies:
      - indexer
      - analyzer
      - tui_base
  - id: cli_arguments
    content: Implement command line arguments parser - --directory, --config, --verbose, --version, --help with proper validation
    status: pending
    dependencies:
      - setup_project
  - id: environment_variables
    content: Implement environment variable support - FILE_SORTER_CONFIG_PATH, FILE_SORTER_LOG_LEVEL, FILE_SORTER_DATA_DIR, FILE_SORTER_LANGUAGE
    status: pending
    dependencies:
      - config_system
      - logging_system
  - id: backup_restore
    content: Implement backup and restore functionality - manual backup procedures, restore from backup, export/import index and config
    status: pending
    dependencies:
      - index_storage
      - version_storage
      - config_system
  - id: data_migration
    content: Implement data migration system - config format migration, index format migration, version history migration, automatic upgrade path
    status: pending
    dependencies:
      - config_validation
      - index_storage
      - version_storage
  - id: release_process
    content: Set up release process - version numbering (semantic versioning), release checklist, CHANGELOG.md management, automated release workflow
    status: pending
    dependencies:
      - ci_cd_pipeline
      - pip_package
  - id: contributing_guidelines
    content: Create detailed contributing guidelines - development workflow, code style guide, testing requirements, pull request process
    status: pending
    dependencies:
      - code_quality
      - testing_framework
  - id: security_audit
    content: Create security audit checklist - pre-release security checks, dependency security, file operations security, privacy security verification
    status: pending
    dependencies:
      - file_operations
      - llm_client
  - id: disaster_recovery
    content: Implement disaster recovery procedures - data loss prevention, corruption detection, recovery tools, index and version repair
    status: pending
    dependencies:
      - checkpoint_manager
      - version_manager
      - index_storage
  - id: accessibility_features
    content: Implement accessibility features - full keyboard navigation, screen reader support, color contrast compliance, text scaling options
    status: pending
    dependencies:
      - tui_base
      - tui_screens
  - id: api_documentation
    content: Create API documentation - core module APIs, TUI component APIs, extension points, code examples
    status: pending
    dependencies:
      - main_integration
      - documentation
---

# File Sorter TUI System - Plan

## System Architecture

```mermaid
flowchart TD
    Start[Program Launch] --> Init[Initialization in English]
    Init --> ConfigCheck[Check Configuration]
    ConfigCheck --> CheckIndexStatus{Check Last Indexing Time}
    CheckIndexStatus -->|No Index/Expired| IndexScreen[Indexing Screen - top-like UI]
    CheckIndexStatus -->|Index Exists| MainScreen[Main Screen - top-like UI]
    IndexScreen --> IndexProcess[Indexing Process - Live Status]
    IndexProcess --> IndexComplete[Indexing Complete]
    IndexComplete --> MainScreen
    MainScreen -->|Functions Blocked| ShowBlocked[Show Blocked Functions Message]
    MainScreen --> Analyze[Analyze with LLM]
    MainScreen --> ViewIndex[View Indexed Files Table]
    MainScreen --> Rollback[Rollback to Version]
    MainScreen --> Privacy[Private Files Management]
    MainScreen --> Help[Help & Guide]
    MainScreen --> ChangeLang[Change Language]
    MainScreen --> Settings[Settings]
    ChangeLang --> LangSelect[Language Selection]
    LangSelect --> MainScreen
    Analyze --> LLMProcess[LLM Processing]
    LLMProcess --> Preview[Preview]
    Preview --> Confirm[Confirm Changes]
    Confirm --> Execute[Execute Changes]
    Execute --> SaveVersion[Save Version]
    SaveVersion --> MainScreen
    Rollback --> SelectVersion[Select Version]
    SelectVersion --> RollbackPreview[Preview]
    RollbackPreview --> RollbackConfirm[Confirm]
    RollbackConfirm --> RollbackExecute[Rollback]
    RollbackExecute --> SaveVersion
    Help --> MainScreen
```

## Project Structure

```
File_Sorter/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Main entry point
│   ├── tui/
│   │   ├── __init__.py
│   │   ├── app.py              # Textual main application
│   │   ├── screens/
│   │   │   ├── __init__.py
│   │   │   ├── main_screen.py  # Main screen - top-like UI with file table
│   │   │   ├── language_select.py  # Language selection (from main screen)
│   │   │   ├── indexing.py     # Indexing screen - real-time status, top-like UI
│   │   │   ├── analysis.py     # LLM analysis screen with privacy control
│   │   │   ├── preview.py      # Changes preview
│   │   │   ├── rollback.py     # Version rollback
│   │   │   ├── privacy.py      # Private files management
│   │   │   ├── help.py         # Help and guide
│   │   │   └── settings.py    # Settings
│   │   └── widgets/
│   │       ├── __init__.py
│   │       ├── file_table.py   # File table widget - sortable, filterable table
│   │       ├── status_header.py # Status header widget - top section with stats
│   │       ├── file_tree.py    # File tree display
│   │       └── version_list.py # Version list
│   ├── core/
│   │   ├── __init__.py
│   │   ├── indexer.py          # File indexing
│   │   ├── analyzer.py         # Surface-level file analysis (magic numbers, metadata, previews)
│   │   ├── llm_client.py       # LLM integration with privacy control
│   │   ├── file_operations.py  # File operations (move, rename)
│   │   ├── version_manager.py  # Version management
│   │   ├── privacy_manager.py  # Private files management and filtering
│   │   └── exceptions_manager.py # Exceptions system (directories/files/extensions to ignore)
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── index_storage.py    # Index storage
│   │   ├── checkpoint_manager.py  # Checkpoint management and resuming
│   │   └── version_storage.py # Version storage JSON
│   ├── i18n/
│   │   ├── __init__.py
│   │   ├── translations.py    # Translation management
│   │   ├── lv.json            # Latvian language
│   │   ├── ru.json            # Russian language
│   │   └── en.json            # English language
│   └── utils/
│       ├── __init__.py
│       ├── config.py           # Configuration management
│       ├── logger.py           # Logging
│       ├── cli.py               # Command line argument parsing
│       ├── backup.py            # Backup and restore utilities
│       └── migration.py         # Data migration utilities
├── .file_sorter/               # Hidden directory (created in working directory)
│   ├── index.json              # Index data (may be split into multiple files for large directories)
│   ├── index_checkpoint.json   # Checkpoint for indexing (progress saving)
│   ├── index_lock              # Lock file to prevent parallel indexing
│   ├── versions/               # Version history (one version per operation)
│   │   ├── v1.json             # Compressed and optimized
│   │   ├── v2.json
│   │   └── ...
│   ├── config.json             # User configuration
│   ├── exceptions.json         # Private files/directories/extensions exceptions
│   └── logs/                   # Log files
│       ├── application.log
│       ├── errors.log
│       └── debug.log
├── requirements.txt
├── requirements-dev.txt        # Development dependencies
├── setup.py                    # Pip package configuration
├── pyproject.toml              # Modern package configuration
├── pytest.ini                  # Pytest configuration
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── .ruff.toml                  # Ruff linting configuration
├── .mypy.ini                   # MyPy type checking configuration
├── pyrightconfig.json          # Pyright configuration (optional)
├── install.sh                  # Linux/MacOS installation script
├── install.bat                 # Windows CMD installation script
├── install.ps1                 # Windows PowerShell installation script
├── scripts/
│   ├── check_python.py         # Python version check
│   └── install_guide.py       # Instruction display
├── tests/
│   ├── __init__.py
│   ├── unit/                   # Unit tests
│   │   ├── __init__.py
│   │   ├── test_indexer.py
│   │   ├── test_analyzer.py
│   │   ├── test_llm_client.py
│   │   ├── test_version_manager.py
│   │   └── test_file_operations.py
│   ├── integration/            # Integration tests
│   │   ├── __init__.py
│   │   ├── test_indexing_workflow.py
│   │   ├── test_llm_workflow.py
│   │   └── test_rollback_workflow.py
│   ├── tui/                    # TUI tests
│   │   ├── __init__.py
│   │   ├── test_main_screen.py
│   │   └── test_indexing_screen.py
│   └── fixtures/               # Test fixtures
│       ├── sample_files/
│       └── mock_responses/
├── docs/
│   ├── user/                   # User documentation
│   │   ├── getting_started.md
│   │   ├── user_guide.md
│   │   └── faq.md
│   ├── developer/              # Developer documentation
│   │   ├── architecture.md
│   │   ├── api.md
│   │   └── contributing.md
│   └── api/                    # API reference
│       ├── core.md
│       └── tui.md
├── .github/
│   ├── workflows/              # GitHub Actions
│   │   ├── ci.yml              # Continuous Integration
│   │   ├── security.yml        # Security scanning
│   │   └── release.yml         # Release workflow
│   ├── ISSUE_TEMPLATE/         # Issue templates
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── CHANGELOG.md                # Changelog
├── CONTRIBUTING.md             # Contributing guidelines
├── SECURITY.md                 # Security policy
├── LICENSE                     # MIT License
├── README.md
└── .gitignore
```

## Main Components

### 1. Indexing System (`core/indexer.py`)

- **Directory Selection and .file_sorter Creation:**
  - On program launch, creates empty `.file_sorter/` directory in current working directory
  - This marks that the tool has been run in this directory
  - By default, tool works only in the opened directory
  - If user opens a subdirectory, checks parent directories for existing `.file_sorter/`
  - If found in parent, offers to use that `.file_sorter/` instead
  - Each directory can have its own `.file_sorter/` or share parent's

- **Indexing only when TUI is opened:**
  - Indexing is **NOT automatic** - user must start it manually from TUI
  - On TUI launch, checks if indexing has been performed
  - If no index exists or indexing incomplete, functions are blocked until indexing is done
  - User clicks "Start Indexing" button to begin indexing process

- **Dynamic Indexing (Pause/Resume):**
  - Indexing can be paused at any time (Ctrl+C or pause button)
  - Progress is saved to checkpoint immediately
  - Can resume from exact point where paused
  - All program state saved quickly and correctly for fast resume

- **Indexing status check:**
  - Checks `index.json` for `indexed_at` timestamp
  - If no index exists: `indexing_status = "not_started"`
  - If indexing incomplete (checkpoint exists): `indexing_status = "in_progress"`
  - If indexing complete: `indexing_status = "completed"`
  - This status determines which functions are available

- **Efficient processing for large file counts (10000+):**
  - Batch processing - processes files in chunks (e.g., 100 files at a time)
  - Parallel processing with `concurrent.futures.ThreadPoolExecutor` (configurable thread count)
  - Real-time progress updates to TUI (every 100-500ms)
  - Optimized memory usage - does not store all files in memory simultaneously

- **Checkpoint system (resume after interruption):**
  - Saves checkpoint after each batch processing (`index_checkpoint.json`)
  - Checkpoint contains:
    - List of processed files (paths)
    - Progress (how many files processed, how many remaining)
    - Timestamp
    - Hash sums for processed files (to detect changes)
  - If program is interrupted, on next launch:
    - Checks for checkpoint existence
    - Shows resume option in indexing screen
    - Determines which files are already processed
    - Resumes from last checkpoint
    - Checks if files have changed (by hash)
    - Updates only changed files

- **Incremental indexing:**
  - After full indexing, saves file hash sums and modification dates
  - On next indexing run:
    - Quickly scans directory structure
    - Compares modification dates with indexed dates
    - Identifies changed files (modified date newer than indexed date)
    - Identifies deleted files (file no longer exists)
    - Identifies new files (not in index)
    - Updates index only with changed/new files
    - Removes deleted files from index
  - Fast comparison using dates first, then hash verification
  - Saves time and resources

- **Lock mechanism:**
  - Uses `index_lock` file to prevent parallel indexing
  - If program is interrupted, lock file is cleared on next launch

- **Recursive directory traversal:**
  - Recursively goes through all directories
  - Indexes file names, paths, sizes, dates
  - Calls `analyzer.py` for surface-level analysis
  - Saves results to `index.json` and checkpoint
  - Updates `indexed_at` timestamp when complete

### 2. Analysis System (`core/analyzer.py`)

- **Surface-level analysis - DOES NOT READ FULL FILES:**
  - Uses file magic numbers (first bytes) for file type detection
  - Reads only first 512-1024 bytes for text files (content preview)
  - Uses `python-magic` or `filetype` libraries for file type detection
  - File size and date information (without reading content)

- **Metadata extraction (only standard metadata, not file content):**
  - Images: EXIF data (date, camera, GPS - only if available)
  - Audio: ID3 tags (artist, album - only tags, not audio content)
  - Documents: only file type detection, not content
  - Archives: only structure, not content

- **Efficiency for large file counts:**
  - Parallel processing with `concurrent.futures.ThreadPoolExecutor` (configurable thread count, default 4-8)
  - Batch processing - processes files in chunks
  - Progress indicator with detailed information (files/s, remaining time)
  - Does not use more memory than necessary - does not store all files in memory
  - For text files reads only first lines (max 10-20 lines) for content preview
  - For large files (>10MB) skips content preview, only metadata
  - Optimization: similar files (by type) processed in groups

- **Checkpoint integration:**
  - Analysis results saved in checkpoint together with index
  - If analysis is interrupted, can resume from last checkpoint

### 3. LLM Integration (`core/llm_client.py`)

- **Privacy and security guarantees:**
  - **EVERYTHING stored locally** - nothing is sent without user permission
  - User can choose what to send to LLM:
    - Option 1: Structure only (file names, directory structure, file types)
    - Option 2: Structure + metadata (without file content)
    - Option 3: Structure + metadata + text file previews (only first lines)
  - **SENSITIVE FILES:** Files marked as private or matching exceptions are **NEVER** sent to LLM
  - Before sending to LLM - **clear warning** and **JSON preview** showing exactly what will be sent
  - User can review and edit JSON payload before sending
  - User can use local LLM (Ollama) - everything stays on computer

- **LLM Request/Response Preview:**
  - **Before sending:** Show exact JSON that will be sent to LLM
  - User can review payload structure
  - User can add custom instructions: "How should I organize these files into folders?"
  - User must explicitly confirm before sending
  - **After receiving:** Show LLM response
  - Validate response format matches expected structure
  - If response is incorrect or dangerous, request LLM to retry with clearer instructions
  - Option to save request/response locally (not prominent, but available)

- **LLM Instructions:**
  - User provides instructions on how to organize files
  - System instructs LLM to return data in specific format:
    - Short and concise response
    - Clear instructions on where to move files
    - How to rename files
    - JSON format only, no explanations in natural language (unless requested)

- **Supports multiple LLM providers:**
  - OpenAI (GPT-4, GPT-3.5) - BYOK (user provides API key, stored securely)
  - Anthropic (Claude) - BYOK (user provides API key, stored securely)
  - Ollama (local LLM) - **RECOMMENDED for privacy** (no API key needed)
  - **Custom LLM endpoint:** User can specify custom endpoint and connection parameters
  - User selects provider and provides API key (stored in config)
  - API keys persist across sessions

- **LLM Provider Selection:**
  - Default: Show only popular providers (OpenAI, Anthropic, Ollama)
  - User selects provider and enters API key
  - API key stored securely in config.json
  - Option for custom LLM endpoint:
    - User specifies endpoint URL
    - User specifies connection parameters
    - Stored in config for future use

- **Fallback Mechanism:**
  - If LLM request fails, show error message
  - Inform user they can choose different LLM provider
  - No automatic fallback - user must explicitly choose

- **Data sent to LLM:**
  - Only file/directory structure (names, types, sizes)
  - Metadata (without sensitive information)
  - User instructions/goals
  - **NEVER:** Full file content, sensitive information, private files, files matching exceptions

- **Returns JSON with recommendations:**
  - Move operations (source → destination)
  - Rename recommendations (old_name → new_name)
  - Directory creation recommendations
  - Response validated against expected format
  - If invalid, request retry with format instructions

### 4. Version Management (`core/version_manager.py`)

- **Version Creation:**
  - Every operation through the tool creates a new version
  - Version count = number of operations performed
  - Versions stored efficiently to avoid system overload
  - Large files avoided - only directory structure saved, not file contents
  - Versions compressed and optimized for storage efficiency

- **Version Storage:**
  - Each version stored in `versions/vN.json`
  - Versions compressed (gzip) to save space
  - Only stores directory structure (paths, names, types) - not file contents
  - LLM recommendations saved with each version
  - Timestamp and operation description included

- **Optimization:**
  - Incremental storage: only stores changes from previous version
  - Compression: gzip compression for version files
  - Cleanup: optional automatic cleanup of old versions (configurable)
  - Smart storage: large directories split into multiple version files if needed

- **Rollback Support:**
  - Full rollback: restore entire directory structure
  - Selective rollback: restore specific files/directories
  - Version comparison: show differences between versions

### 5. TUI Interface (`tui/app.py` and screens/)

- **Main Screen (`tui/screens/main_screen.py`) - "top" like interface:**
  - **Layout similar to Linux "top" command:**
    - **Top section (header):** System information and settings
      - Last indexing time and status
      - Total files indexed
      - Files processed / remaining
      - Current indexing status (if in progress)
      - System stats (memory usage, processing speed)
      - Quick actions (keyboard shortcuts visible)
    - **Bottom section (main area):** File list table
      - All indexed files displayed in table format
      - Columns: Name, Path, Type, Size, Status, Last Modified
      - Sortable columns
      - Filterable by type, status, etc.
      - Real-time updates during indexing
      - Scrollable list
  
  - **Indexing Status Check:**
    - On TUI launch, checks when last indexing was performed
    - If no index exists or indexing never completed:
      - All related functions are **BLOCKED** (grayed out, disabled)
      - Shows message: "Indexing required - functions will be available after indexing"
      - Only indexing function is available
    - If index exists:
      - All functions are available
      - Shows last indexing timestamp
  
  - **Function Blocking:**
    - When indexing is not complete, these functions are blocked:
      - Analyze with LLM
      - View Index (shows empty state)
      - Rollback to Version
      - Private Files Management
    - Only available functions:
      - Start Indexing
      - Settings
      - Help & Guide
      - Change Language

- **Indexing Screen (`tui/screens/indexing.py`) - Real-time status:**
  - **"top" like layout:**
    - **Top section:** Indexing progress and statistics
      - Current status: "Indexing in progress..." or "Resuming from checkpoint..."
      - Progress bar with percentage
      - Files processed / total files
      - Processing speed (files/s)
      - Estimated remaining time
      - Current batch number / total batches
      - Memory usage
      - Thread count and CPU usage
    - **Bottom section:** Live file processing table
      - Shows files currently being processed
      - Columns: File Name, Status (Processing/Completed/Error), Progress
      - Real-time updates as files are processed
      - Scrollable list
      - Color coding: green (completed), yellow (processing), red (error)
  
  - **Real-time Updates:**
    - Updates every 100-500ms during indexing
    - Shows which files are currently being analyzed
    - Displays errors if any occur
    - **While indexing:** Other operations blocked, only progress display active
    - Can pause/resume indexing (checkpoint supported)
    - Pause saves state immediately for fast resume
  
  - **Completion:**
    - When indexing completes, automatically transitions to main screen
    - Shows summary: "Indexing complete - X files indexed"
    - Unblocks all functions

- **File Table Widget (`tui/widgets/file_table.py`):**
  - Displays indexed files in table format
  - **Multi-select support:** User can select multiple files for batch operations
  - **Smart search:** Search by name, type, or content preview
    - Multi-language search support
    - Fuzzy matching
    - Real-time search filtering
  - **Detailed file info:** Optional detailed view (metadata, preview)
    - Table shows only essential info (like file explorers)
    - User can open detailed view for specific file
    - Detailed view shows: full metadata, content preview, file path, etc.
  - Sortable columns (click header to sort)
  - Filterable (by type, status, etc.)
  - **Virtualization:** For large tables (10000+ rows)
    - Only renders visible rows
    - Efficient scrolling
    - No system overload
  - Real-time updates during indexing
  - Pagination for very large file counts
  - Color coding for file types
  - **Ignored files section:** Shows files matching exceptions in separate section

- **Help Screen (`tui/screens/help.py`):**
  - Detailed guide for program usage
  - Sections: getting started, indexing, LLM analysis, version control, privacy
  - Keyboard shortcuts
  - Frequently asked questions (FAQ)
  - Multi-language support

- **Language Selection (`tui/screens/language_select.py`):**
  - Available from main screen
  - Can be changed at any time
  - Languages: English, Latvian, Russian
  - Changes immediately apply to entire UI

- Textual base application
- Screens for various functions
- Interactive navigation
- Multi-language support in all texts
- Real-time updates with Textual's reactive system

### 6. Translation System (`i18n/`)

- **English by default:**
  - Program starts with English
  - No initial language selection needed
  - User can change language at any time from main menu

- JSON files for each language support:
  - `en.json` - English (default)
  - `lv.json` - Latvian
  - `ru.json` - Russian

- Dynamic language switching:
  - Changes immediately apply to entire UI
  - User choice saved in configuration
  - Next launch uses saved language

- All UI texts translated:
  - Main menu
  - All screens
  - Error messages
  - Help text
  - Warnings and confirmations

## Data Structures

### Index Structure (`index.json`)

```json
{
  "version": "1.0",
  "root_path": "/path/to/target",
  "indexed_at": "2024-01-01T12:00:00",
  "indexing_status": "completed",
  "total_files": 10000,
  "total_directories": 500,
  "indexing_duration_seconds": 120,
  "files": [
    {
      "path": "relative/path/to/file.txt",
      "name": "file.txt",
      "size": 1024,
      "modified": "2024-01-01T10:00:00",
      "file_type": "text/plain",
      "mime_type": "text/plain",
      "magic_number": "text",
      "content_preview": "First 10-20 lines or first 512 bytes",
      "metadata": {
        "encoding": "utf-8",
        "line_count": 150
      },
      "is_private": false,
      "summary": "Summary from metadata and preview"
    },
    {
      "path": "relative/path/to/image.jpg",
      "name": "image.jpg",
      "size": 2048000,
      "modified": "2024-01-01T10:00:00",
      "file_type": "image/jpeg",
      "mime_type": "image/jpeg",
      "magic_number": "JPEG",
      "content_preview": null,
      "metadata": {
        "width": 1920,
        "height": 1080,
        "camera": "Canon EOS",
        "date_taken": "2023-12-01"
      },
      "is_private": false,
      "summary": "Photograph, 1920x1080"
    }
  ],
  "directories": [
    {
      "path": "relative/path/to/dir",
      "name": "dir",
      "file_count": 10,
      "total_size": 10485760,
      "summary": "Summary from file types and names"
    }
  ]
}
```

**Important:** `content_preview` contains only a sample (max 512-1024 bytes or 10-20 lines), not full file content. For large files preview may be empty or minimal.

### Version Structure (`versions/vN.json`)

```json
{
  "version": 1,
  "created_at": "2024-01-01T12:00:00",
  "description": "Initial structure",
  "file_structure": {
    "files": [...],
    "directories": [...]
  },
  "llm_suggestions": null
}
```

### Checkpoint Structure (`index_checkpoint.json`)

```json
{
  "checkpoint_version": "1.0",
  "started_at": "2024-01-01T12:00:00",
  "last_updated": "2024-01-01T12:30:00",
  "root_path": "/path/to/target",
  "total_files": 10000,
  "processed_files": 7500,
  "remaining_files": 2500,
  "processed_paths": [
    "relative/path/to/file1.txt",
    "relative/path/to/file2.jpg",
    ...
  ],
  "file_hashes": {
    "relative/path/to/file1.txt": "abc123...",
    "relative/path/to/file2.jpg": "def456...",
    ...
  },
  "current_batch": 75,
  "total_batches": 100,
  "batch_size": 100,
  "status": "in_progress",
  "errors": []
}
```

**Checkpoint usage:**
- Saves progress after each batch processing
- Allows resuming from last checkpoint if program is interrupted
- Hash sums allow determining if files have changed
- If file has changed, it is reprocessed
- State saved quickly and correctly for fast resume

### Exceptions Structure (`exceptions.json`)

```json
{
  "version": "1.0",
  "directories": [
    "/path/to/private/dir",
    "relative/path/to/another/dir"
  ],
  "files": [
    "/path/to/private/file.txt",
    "relative/path/to/another/file.pdf"
  ],
  "extensions": [
    ".pdf",
    ".docx",
    ".xlsx"
  ],
  "patterns": [
    "*secret*",
    "*private*"
  ]
}
```

**Exceptions usage:**
- Files/directories matching exceptions are **ignored** during indexing
- Not sent to LLM analysis
- Displayed in separate "Ignored Files" section in file table
- Persist across sessions
- Can be managed through TUI

### Index Optimization

- **Index Size Management:**
  - Index files optimized to avoid system overload
  - For very large directories (10000+ files), index can be split into multiple files
  - Split by directory or by file count (configurable)
  - Each split file contains subset of index data
  - Logic remains intact for LLM processing (all data accessible)

- **Index Compression:**
  - Optional compression (gzip) for index files
  - Reduces disk space usage
  - Decompression handled transparently
  - Compression level configurable (speed vs. size tradeoff)

- **Index Storage Format:**
  - JSON format for readability and debugging
  - Efficient structure to minimize file size
  - Only essential data stored (no redundant information)
  - Incremental updates only store changes

### LLM Recommendation Structure

```json
{
  "operations": [
    {
      "type": "move",
      "source": "old/path/file.txt",
      "destination": "new/path/file.txt"
    },
    {
      "type": "rename",
      "source": "old_name.txt",
      "destination": "new_name.txt"
    },
    {
      "type": "create_directory",
      "path": "new/category/"
    }
  ],
  "reasoning": "Explanation why such changes"
}
```

## Workflow

1. **Initial Launch:**
   - Program starts with **English by default**
   - **Directory Selection:**
     - Program runs in current working directory (where it's launched)
     - Creates empty `.file_sorter/` directory in current directory
     - This marks that tool has been run in this directory
     - **By default:** Tool works only in opened directory
     - **If user opens subdirectory:**
       - Check parent directories for existing `.file_sorter/`
       - If found in parent, offer to use that `.file_sorter/` instead
       - User can choose: use parent's `.file_sorter/` or create new one
   - **Opens TUI immediately** - no automatic indexing
   - **Indexing status check on TUI launch:**
     - Reads `index.json` to get `indexed_at` timestamp and `indexing_status`
     - Checks if checkpoint exists (incomplete indexing)
     - **If no index exists or indexing never completed:**
       - Shows main screen with **all functions BLOCKED** (grayed out, disabled)
       - Displays message in header: "Indexing required - Please start indexing first"
       - Shows empty file table with "Start Indexing" button
       - Only available functions: Start Indexing, Settings, Help, Change Language
     - **If index exists and complete:**
       - Shows main screen with all functions available
       - Displays last indexing timestamp in header
       - Shows file table with all indexed files
     - **If checkpoint exists (incomplete indexing):**
       - Shows main screen with functions blocked
       - Shows resume option: "Resume indexing from checkpoint"
       - User can resume or start fresh

2. **Main Screen (top-like interface):**
   - **Top section (header):**
     - Last indexing time and status
     - Total files indexed
     - System statistics (memory, CPU)
     - Quick actions and keyboard shortcuts
   - **Bottom section (main area):**
     - **If indexing not done:** Shows empty state with "Start Indexing" button
     - **If indexing done:** Shows file table with all indexed files
       - Table columns: Name, Path, Type, Size, Status, Last Modified
       - Sortable and filterable
       - Real-time updates
   - **Function availability:**
     - **If indexing not complete:** Functions are BLOCKED (grayed out)
       - Analyze with LLM - BLOCKED
       - View Index - Shows empty state
       - Rollback to Version - BLOCKED
       - Private Files Management - BLOCKED
     - **If indexing complete:** All functions available
     - Always available: Start Indexing, Settings, Help, Change Language

3. **Indexing Screen (real-time status, top-like interface):**
   - **Layout:**
     - **Top section:** Indexing progress and statistics
       - Current status: "Indexing in progress..." or "Resuming from checkpoint..."
       - Progress bar with percentage
       - Files processed / total files
       - Processing speed (files/s)
       - Estimated remaining time
       - Current batch number / total batches
       - Memory usage
       - Thread count and CPU usage
       - Last checkpoint time (if resuming)
     - **Bottom section:** Live file processing table
       - Shows files currently being processed
       - Columns: File Name, Status (Processing/Completed/Error), Progress, File Type
       - Real-time updates every 100-500ms
       - Scrollable list
       - Color coding: green (completed), yellow (processing), red (error)
       - Shows which files are in current batch
   - **Checkpoint check:**
     - Checks if `index_checkpoint.json` exists
     - If exists and not complete, shows resume option in header
     - If resuming, loads checkpoint and continues from last batch
     - Displays checkpoint info in top section
   - **Efficient processing for large file counts (10000+):**
     - Recursively goes through directory
     - Processes files in batches (default 100 files per batch)
     - Parallel processing with ThreadPoolExecutor (configurable thread count)
     - Performs surface-level analysis for each file (only metadata, not full content)
     - For large files (>10MB) skips content preview
     - **Real-time UI updates:** Updates table as each file is processed
   - **Checkpoint saving:**
     - Saves checkpoint after each batch processing
     - Saves list of processed files and hash sums
     - Progress information (how many processed, how many remaining)
     - If program is interrupted (Ctrl+C, system error), checkpoint is saved
     - Updates UI header with checkpoint status
   - **Real-time status display:**
     - Progress bar updates continuously
     - File table updates as files are processed
     - Statistics update in real-time (files/s, remaining time)
     - Shows current batch progress
     - Displays errors if any occur
   - **Resume after interruption:**
     - On next launch checks checkpoint
     - Shows resume option in indexing screen
     - Determines which files are already processed
     - Checks hash sums to determine changed files
     - Continues processing from last checkpoint
     - Updates only changed files
     - Shows resume status in header
   - **Completion:**
     - When everything is processed, saves full index
     - Updates `indexed_at` timestamp in index.json
     - Deletes checkpoint file
     - Saves file hash sums for incremental indexing
     - **Automatically transitions to main screen**
     - Shows completion message: "Indexing complete - X files indexed"
     - **Unblocks all functions** on main screen

4. **LLM Analysis:**
   - **LLM Provider Selection:**
     - User selects LLM provider (OpenAI, Anthropic, Ollama, or Custom)
     - User enters API key (stored securely in config)
     - For custom LLM: user specifies endpoint and connection parameters
     - API keys persist across sessions
   - **Request Preparation:**
     - User enters goals/instructions: "How should I organize these files into folders?"
     - User can add custom instructions for LLM
     - Chooses what to send to LLM (structure, metadata, or previews)
     - Private files and exceptions are **NEVER** sent
     - **JSON Preview:** Shows exact JSON that will be sent to LLM
     - User can review payload before sending
     - Clear warning before sending
     - User must explicitly confirm before sending
   - **Sending Request:**
     - Sends summary to LLM
     - Shows progress indicator
     - If request fails, shows error and allows choosing different provider
   - **Response Handling:**
     - Receives organization plan from LLM
     - **Response Validation:**
       - Validates response format matches expected structure
       - Checks for required fields (operations, source, destination)
       - If response is incorrect or dangerous:
         - Request LLM to retry with clearer instructions
         - Show format requirements to LLM
         - LLM must return short, concise response with clear instructions
     - **Response Preview:**
       - Shows LLM response to user
       - User can review before applying
     - **Save Request/Response (Optional):**
       - Option to save request and response locally
       - Not prominent, but available
       - Saved in `.file_sorter/logs/` or similar location

5. **Preview and Execution:**
   - Shows planned changes (move, rename, create directory)
   - **Conflict Detection:**
     - Checks if destination file already exists
     - Checks for symlinks and hard links
     - Detects permission issues
     - Shows conflicts before execution
   - **Conflict Resolution:**
     - **File already exists at destination:**
       - Ask user: overwrite, skip, or rename
       - Show both files for comparison
       - User chooses action (same logic reused for all conflicts)
     - **Symlinks:**
       - Ask user: follow symlink, ignore, or treat as regular file
       - Save preference in config
     - **Hard Links:**
       - Ask user: treat as separate file, maintain link, or skip
       - Explain implications
       - Save preference in config
   - User confirms all operations
   - Executes changes atomically (all or nothing)
   - Creates new version after successful execution
   - Saves version with operation description

6. **Rollback:**
   - Shows version list
   - User selects version
   - Restores file structure

7. **Language Change:**
   - Available from main menu
   - User selects language (English, Latvian, Russian)
   - Changes immediately apply to entire UI
   - Saved in configuration

8. **Help:**
   - Available from main menu or F1/'?' key
   - Detailed guide
   - FAQ section
   - Keyboard shortcuts

## Technical Details

- **Python version:** 3.10+
- **Main libraries:**
  - `textual` - TUI framework
  - `rich` - Formatted output (Textual dependency)
  - `aiofiles` - Async file operations
  - `httpx` - LLM API calls (more modern than aiohttp)
  - `python-magic` or `filetype` - File type detection by magic numbers (efficient, no need to read entire file)
  - `Pillow` (PIL) - Image EXIF metadata extraction (metadata only)
  - `mutagen` - Audio file ID3 tag extraction (tags only)
  - `python-docx` - DOCX file basic info (structure only, not content)
  - `PyPDF2` or `pypdf` - PDF file basic info (metadata only)
  - `concurrent.futures` - Parallel file processing (built-in Python)
  - `hashlib` - File hash sum calculation for checkpoint system (built-in Python)

- **Configuration:**
  - LLM API key stored in `config.json` (not committed)
  - Settings: LLM provider, model, maximum context
  - Indexing settings: batch_size, thread_count, max_file_size_for_preview

## Performance and Optimization

### Large File Count Processing (10000+)

- **Batch processing:**
  - Processes files in chunks (default 100 files per batch)
  - Configurable batch_size (can increase/decrease depending on system)
  - Saves checkpoint after each batch

- **Parallel processing:**
  - Uses `ThreadPoolExecutor` with configurable thread count
  - Default 4-8 threads (depending on CPU core count)
  - Optimized to not overload system

- **Memory optimization:**
  - Does not store all files in memory simultaneously
  - Processes files in batches
  - For large files (>10MB) skips content preview
  - Garbage collection after each batch

- **Progress monitoring:**
  - Real-time progress indicator
  - Average processing speed (files/s)
  - Estimated remaining time
  - Memory usage monitoring

### Checkpoint and Resuming

- **Checkpoint mechanism:**
  - Automatically saves progress after each batch
  - Saves list of processed files and hash sums
  - If program is interrupted, checkpoint is saved

- **Resume after interruption:**
  - On next launch automatically detects checkpoint
  - Asks user if to resume from checkpoint
  - Continues processing from last batch
  - Checks hash sums to determine changed files
  - Updates only changed files

- **Lock mechanism:**
  - Prevents parallel indexing
  - If program is interrupted, lock file is cleared on next launch

### Incremental Indexing

- **Date-based comparison:**
  - After full indexing saves file hash sums and modification dates
  - On next launch:
    - Quickly scans directory structure
    - Compares modification dates with indexed dates
    - Identifies changed files (modified date newer than indexed date)
    - Identifies deleted files (file no longer exists)
    - Identifies new files (not in index)
    - Updates index only with changed/new files
    - Removes deleted files from index
  - Fast comparison using dates first, then hash verification
  - Saves time and resources

- **File Change Detection:**
  - If file modified outside tool (after indexing):
    - Detected by comparing modification dates
    - File re-indexed automatically
    - Index updated with new data
  - If file deleted outside tool (after indexing):
    - Detected during incremental indexing
    - File removed from index
    - No orphaned entries in index

## Multi-language Support

- **English by default:**
  - Program starts with English
  - No initial language selection needed
  - User can change language at any time from main menu

- All UI texts from JSON files:
  - `en.json` - English (default)
  - `lv.json` - Latvian
  - `ru.json` - Russian

- Language switching:
  - Available from main menu
  - Changes immediately apply to entire UI
  - Saved in configuration

- Example `en.json` (default):
```json
{
  "main_menu": {
    "title": "File Sorter - Main Menu",
    "analyze": "Analyze with LLM",
    "view_index": "View Index",
    "rollback": "Rollback to Version",
    "privacy": "Manage Private Files",
    "help": "Help & Guide",
    "change_language": "Change Language",
    "settings": "Settings"
  },
  "help": {
    "title": "Help & Guide",
    "sections": {
      "getting_started": "Getting Started",
      "indexing": "Indexing Files",
      "llm_analysis": "LLM Analysis",
      "version_control": "Version Control",
      "privacy": "Privacy & Security"
    }
  }
}
```

- Example `lv.json`:
```json
{
  "main_menu": {
    "title": "Failu Kārtošana - Galvenā izvēlne",
    "analyze": "Analizēt ar LLM",
    "view_index": "Skatīt indeksu",
    "rollback": "Atgriezties pie versijas",
    "privacy": "Privātu failu pārvaldība",
    "help": "Palīdzība un pamācība",
    "change_language": "Mainīt valodu",
    "settings": "Iestatījumi"
  }
}
```

## Version Control

- Each change creates a new version
- Versions numbered sequentially
- Saves full structure (not just diff)
- Rollback performs file operations to restore structure
- Selective rollback allows choosing specific files/directories

## Security and Privacy

### File Operation Security

- Does not make changes without confirmation
- Always saves version before changes
- Validation before file operations
- Error handling with rollback to previous version

### Privacy Guarantees

- **EVERYTHING stored locally:**
  - Index stored only in `.file_sorter/` directory on user's computer
  - Version history stored locally
  - No external server calls without user permission
  - No telemetry or analytics

- **File analysis:**
  - **DOES NOT READ FULL FILES** - only surface-level analysis
  - Text files: only first 10-20 lines or 512-1024 bytes
  - Binary files: only metadata (EXIF, ID3 tags)
  - Large files: only file type and size, without reading content

- **LLM integration and privacy:**
  - User **fully controls** what to send to LLM
  - Before sending - clear warning about what will be sent
  - Options:
    - Structure only (file names, directories, types) - **RECOMMENDED**
    - Structure + metadata (without content)
    - Structure + metadata + text previews (only first lines)
  - **Private file/directory marking:**
    - User can mark directories/files as "private" **after indexing** (when files visible in TUI)
    - Private files **NEVER** sent to LLM
    - Private files not included in LLM analysis
    - Private file marks persist across sessions
  
  - **Exceptions System:**
    - User can create global exceptions:
      - Mark entire directories as private/ignored
      - Mark specific files as private/ignored
      - Mark file extensions as private/ignored (e.g., all .pdf files)
      - Use patterns (e.g., *secret*, *private*)
    - Exceptions stored in `exceptions.json`
    - Files matching exceptions are:
      - **Ignored during indexing** (skipped)
      - **Not sent to LLM** (filtered out)
      - **Displayed in separate "Ignored Files" section** in file table
    - Exceptions persist across sessions
    - Can be managed through TUI (add, remove, edit exceptions)

- **Local LLM (Ollama) - maximum privacy:**
  - Recommended to use Ollama local LLM
  - All processing happens on user's computer
  - No internet connection needed
  - No data sending to external servers

- **Data storage:**
  - Configuration stored locally (`config.json`)
  - LLM API keys stored locally (never committed)
  - No log sending to external servers
  - All data stays on user's computer

### Efficient File Processing

- **Magic number identification:**
  - Uses `python-magic` or `filetype` libraries
  - Reads only first bytes (file header) for file type detection
  - No need to read entire file

- **Parallel processing:**
  - For large directories uses `concurrent.futures.ThreadPoolExecutor`
  - Progress indicator
  - Optimized memory usage

- **Metadata extraction:**
  - Images: EXIF data (metadata only, not image content)
  - Audio: ID3 tags (tags only, not audio content)
  - Documents: only file type, not content
  - Archives: only structure, not content

### Checkpoint Security and Reliability

- **Checkpoint integrity:**
  - Hash sums for processed files (SHA-256)
  - Checkpoint file structure validation
  - If checkpoint is corrupted, starts fresh with warning

- **Resume security:**
  - Checks if files have changed (by hash)
  - If file has changed, reprocesses
  - Validation before resuming
  - Error handling - if resume fails, starts fresh

- **Lock mechanism:**
  - Prevents parallel indexing
  - Automatic lock cleanup if program is interrupted
  - Timeout mechanism - if lock is old (>1 hour), it is cleared

- **Data storage:**
  - Checkpoint stored only locally
  - No data sending to external servers
  - Checkpoint contains only file paths and hash sums (not file content)

## Installation System

### Installation Scripts

Program will be distributed with installation scripts for all operating systems:

1. **Linux/MacOS:** `install.sh`
   - Checks for Python 3.10+ presence
   - If no Python, shows detailed instructions with link to python.org
   - Installs pip if not present
   - Installs program with `pip install -e .`
   - Creates `file-sorter` command in system

2. **Windows CMD:** `install.bat`
   - Checks for Python presence
   - If not, opens browser with python.org and shows instructions
   - Installs program

3. **Windows PowerShell:** `install.ps1`
   - Same functionality as install.bat
   - Supports PowerShell specific features

### Installation Process

```mermaid
flowchart TD
    Start[User runs install.sh/bat/ps1] --> CheckPython{Python installed?}
    CheckPython -->|Yes| CheckVersion{Python >= 3.10?}
    CheckPython -->|No| ShowGuide[Show installation instructions]
    ShowGuide --> OpenBrowser[Open python.org in browser]
    ShowGuide --> Exit[Exit with instructions]
    CheckVersion -->|Yes| CheckPip{pip installed?}
    CheckVersion -->|No| ShowUpgrade[Show how to upgrade Python]
    CheckPip -->|Yes| InstallPackage[Install file-sorter with pip]
    CheckPip -->|No| InstallPip[Install pip]
    InstallPip --> InstallPackage
    InstallPackage --> CreateCommand[Create file-sorter command]
    CreateCommand --> Success[Installation complete]
    Success --> RunApp[Launch program]
```

### Pip Package (`setup.py` / `pyproject.toml`)

Program will be available as pip package:
- Installation: `pip install file-sorter` or `pip install -e .` (development)
- Launch: `file-sorter` command in any terminal
- Entry point: `src/main.py` as `file-sorter` command

### Python Version Check (`scripts/check_python.py`)

- Checks Python version (minimum 3.10)
- Checks pip presence
- Returns detailed error message if something is wrong
- Multi-language error messages

### Installation Instructions (`scripts/install_guide.py`)

- Shows detailed instructions how to install Python
- Separate instructions for each OS (Windows, Linux, MacOS)
- Multi-language instructions
- Links to official downloads

### Usage After Installation

After installation user can:
1. Open terminal
2. Type `file-sorter`
3. Program launches and asks to select directory to work with

### Simple Installation Command

Users can install with one command:

**Linux/MacOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/user/file-sorter/main/install.sh | bash
```

**Windows PowerShell:**
```powershell
iwr -useb https://raw.githubusercontent.com/user/file-sorter/main/install.ps1 | iex
```

**Or manually:**
- Download `install.sh` / `install.bat` / `install.ps1`
- Run it in terminal

## Error Handling and Logging

### Error Handling System (`core/error_handler.py`)

- **Graceful Error Recovery:**
  - File operation errors: Rollback to previous version automatically
  - LLM API errors: Retry with exponential backoff, fallback options
  - Indexing errors: Skip problematic files, continue with rest, log errors
  - Network errors: Clear error messages, retry options

- **User-Friendly Error Messages:**
  - Multi-language error messages
  - Clear explanations of what went wrong
  - Actionable suggestions for resolution
  - Error codes for troubleshooting

- **Transaction Rollback:**
  - If file operation fails mid-execution, rollback all changes
  - Maintain version consistency
  - Preserve user data integrity

### Logging System (`utils/logger.py`)

- **Structured Logging:**
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Structured format: JSON or key-value pairs
  - Context information: operation, file path, user action

- **Log Storage:**
  - Logs stored in `.file_sorter/logs/` directory
  - Log rotation: daily rotation, keep last 30 days
  - Separate log files: application.log, errors.log, debug.log

- **Debug Mode:**
  - Enable with `--verbose` flag or config option
  - Detailed operation logging
  - Performance metrics logging
  - LLM request/response logging (with privacy filters)

## Atomic Operations and Transaction Safety

### File Operation Atomicity (`core/file_operations.py`)

- **Transaction-Like Behavior:**
  - All file operations grouped into transactions
  - Either all succeed or all rollback
  - No partial state changes
  - Fast and correct state saving for pause/resume capability

- **Operation Validation:**
  - Pre-flight checks before execution:
    - File existence verification
    - Permission checks (skip files without read permissions - IGNORED)
    - Disk space verification
    - Path validation (no conflicts)

- **Conflict Resolution:**
  - **File already exists at destination:**
    - Ask user what to do: overwrite, skip, or rename
    - Show both files (source and destination) for comparison
    - User chooses action before proceeding
    - Same logic reused for all conflict scenarios
  
  - **Symbolic Links (Symlinks):**
    - Ask user what to do: follow symlink, ignore symlink, or treat as regular file
    - Default: follow symlink (but ask first time)
    - User preference saved in config for future operations
  
  - **Hard Links:**
    - Ask user what to do: treat as separate file, maintain link, or skip
    - Explain implications of each choice
    - User preference saved in config

- **Permission Handling:**
  - Files without read permissions: **IGNORED** (skipped during indexing)
  - Log skipped files for user review
  - Continue processing other files
  - Show summary of skipped files at end
  - Display ignored files in separate section of file table

- **Network Drives:**
  - Allow operations on network drives if file system commands work
  - Depends on where program is launched
  - Test file operations before proceeding
  - Warn user about potential performance issues
  - Use same commands as for local files

- **Large Files:**
  - Process intelligently - only metadata, not content
  - No need to read full file contents
  - Use file system metadata where possible
  - Handle files larger than available memory gracefully
  - Skip content preview for large files entirely

- **Rollback on Failure:**
  - If any operation fails, rollback all operations in transaction
  - Restore from version snapshot
  - Clear error message to user

### Operation Ordering

- **Safe Execution Order:**
  1. Create new directories first
  2. Move files (not rename yet)
  3. Rename files last
  4. Delete empty directories last

- **Conflict Detection:**
  - Check for path conflicts before execution
  - Warn user about overwrites
  - Require explicit confirmation for destructive operations
  - Show conflict resolution dialog with options

## Configuration Validation

### Configuration Schema (`utils/config_validator.py`)

- **Schema Validation:**
  - JSON schema for config file structure
  - Type validation for all fields
  - Range validation (e.g., thread_count: 1-32)
  - Enum validation (e.g., language: en/lv/ru)

- **Default Values:**
  - Sensible defaults for all configuration options
  - Auto-generate config if missing
  - Migrate old config formats automatically

- **Validation Error Messages:**
  - Clear error messages for invalid config
  - Suggestions for fixing errors
  - Multi-language error messages

## Keyboard Shortcuts System

### Global Shortcuts

- `F1` or `?` - Show help
- `Ctrl+C` - Cancel current operation
- `q` or `Q` - Quit application
- `Esc` - Go back/Cancel
- `Ctrl+R` - Refresh current view
- `Ctrl+S` - Save current state

### Context-Aware Shortcuts

- **File Table:**
  - Arrow keys - Navigate rows
  - `Enter` - Select file / Open detailed view
  - `Space` - Toggle selection (multi-select)
  - `/` - Focus search
  - `Ctrl+A` - Select all visible files
  - `Ctrl+D` - Deselect all
  - `Tab` - Switch between sections (indexed files / ignored files)
  - `s` - Sort menu
  - `f` - Filter menu

- **Indexing Screen:**
  - `p` - Pause indexing
  - `r` - Resume indexing
  - `c` - Cancel indexing

- **Preview Screen:**
  - `y` - Confirm changes
  - `n` - Reject changes
  - `e` - Edit selection

### Customizable Shortcuts

- Shortcuts configurable in `config.json`
- User-defined key bindings
- Export/import shortcut configurations

## Testing Strategy

### Unit Tests (`tests/unit/`)

- **Core Components:**
  - Indexer tests: batch processing, checkpoint saving
  - Analyzer tests: file type detection, metadata extraction
  - Version manager tests: version creation, rollback
  - LLM client tests: request formatting, response parsing
  - File operations tests: move, rename, validation

- **Test Coverage:**
  - Aim for 80%+ code coverage
  - Critical paths: 100% coverage
  - Edge cases: file permissions, disk full, network errors

### Integration Tests (`tests/integration/`)

- **End-to-End Workflows:**
  - Full indexing workflow
  - LLM analysis workflow
  - Rollback workflow
  - Error recovery workflows

- **Test Fixtures:**
  - Sample file structures
  - Mock LLM responses
  - Test data generators

### TUI Testing (`tests/tui/`)

- **Screen Tests:**
  - Screen rendering tests
  - Navigation tests
  - Widget interaction tests

- **Textual Testing:**
  - Use Textual's testing framework
  - Simulate user interactions
  - Verify UI state changes

## CI/CD Pipeline

### GitHub Actions Workflow (`.github/workflows/`)

- **On Push/PR:**
  - Run unit tests
  - Run integration tests
  - Code quality checks (black, ruff, mypy)
  - Security scanning (CodeQL, Dependabot)

- **On Release:**
  - Build distribution packages
  - Run full test suite
  - Create GitHub release
  - Publish to PyPI (if configured)

### Automated Security Scanning

- **CodeQL Analysis:**
  - Runs on every push
  - Reports security vulnerabilities
  - Blocks PR if critical issues found

- **Dependabot:**
  - Automatic dependency updates
  - Security advisory alerts
  - Automated PR creation

## Code Quality

### Formatting and Linting

- **Black:**
  - Code formatting
  - Line length: 88 characters
  - Consistent style across codebase

- **Ruff:**
  - Fast Python linter
  - Catches common errors
  - Style guide enforcement

- **MyPy:**
  - Static type checking
  - Type hints throughout codebase
  - Gradual typing adoption

### Pre-commit Hooks

- **Automated Checks:**
  - Run black before commit
  - Run ruff before commit
  - Run mypy before commit
  - Run tests before commit (optional)

## Documentation Structure

### User Documentation (`docs/user/`)

- **Getting Started Guide:**
  - Installation instructions
  - First-time setup
  - Basic usage examples
  - Quick start tutorial

- **User Guide:**
  - Feature documentation
  - Common workflows
  - Troubleshooting guide
  - Best practices

- **FAQ:**
  - Frequently asked questions
  - Common issues and solutions
  - Performance tips

- **Video Tutorials:**
  - Installation walkthrough
  - Basic usage tutorial
  - Advanced features tutorial

### Developer Documentation (`docs/developer/`)

- **Architecture Documentation:**
  - System architecture overview
  - Component descriptions
  - Data flow diagrams

- **API Documentation:**
  - Core module APIs
  - TUI component APIs
  - Extension points

- **Contributing Guide:**
  - Development setup
  - Code style guide
  - Testing guidelines
  - Pull request process

## Performance Monitoring

### Operation Timing

- **Metrics Collection:**
  - Indexing duration
  - File analysis time per file
  - LLM API response time
  - File operation duration

- **Performance Display:**
  - Show in UI header during operations
  - Average processing speed
  - Estimated completion time

### Memory Usage Tracking

- **Memory Monitoring:**
  - Track memory usage during indexing
  - Alert if memory usage high
  - Optimize batch size based on available memory

### Performance Optimization

- **Bottleneck Identification:**
  - Profile slow operations
  - Identify optimization opportunities
  - Cache frequently accessed data

## Command Line Interface

### Command Line Arguments

- **`--directory` / `-d`**: Specify target directory to work with
  - Example: `file-sorter --directory /path/to/directory`
  - If not specified, prompts user in TUI

- **`--config` / `-c`**: Specify custom config file path
  - Example: `file-sorter --config /path/to/config.json`
  - Default: `.file_sorter/config.json` in target directory

- **`--verbose` / `-v`**: Enable verbose logging
  - Shows detailed operation logs
  - Useful for debugging
  - Example: `file-sorter --verbose`

- **`--version`**: Show version information
  - Displays version number and exit
  - Example: `file-sorter --version`

- **`--help` / `-h`**: Show help message
  - Displays usage information and exit
  - Example: `file-sorter --help`

- **`--no-tui`**: Run in non-interactive mode (future feature)
  - For scripting and automation
  - Requires all parameters to be provided via CLI

### Environment Variables

- **`FILE_SORTER_CONFIG_PATH`**: Override default config file location
  - Example: `export FILE_SORTER_CONFIG_PATH=/custom/path/config.json`

- **`FILE_SORTER_LOG_LEVEL`**: Set logging level
  - Values: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Example: `export FILE_SORTER_LOG_LEVEL=DEBUG`

- **`FILE_SORTER_DATA_DIR`**: Override default data directory (`.file_sorter/`)
  - Example: `export FILE_SORTER_DATA_DIR=/custom/data/path`

- **`FILE_SORTER_LANGUAGE`**: Set default language
  - Values: en, lv, ru
  - Example: `export FILE_SORTER_LANGUAGE=lv`

## Backup and Restore Procedures

### Manual Backup

- **Backup Index:**
  - Copy `.file_sorter/index.json` to backup location
  - Contains all indexed file metadata

- **Backup Versions:**
  - Copy `.file_sorter/versions/` directory
  - Contains all version snapshots for rollback

- **Backup Configuration:**
  - Copy `.file_sorter/config.json`
  - Contains user settings and API keys

- **Complete Backup:**
  - Copy entire `.file_sorter/` directory
  - Preserves all data including checkpoints

### Restore Procedures

- **Restore from Backup:**
  1. Stop File Sorter if running
  2. Copy backup files to `.file_sorter/` directory
  3. Verify file permissions
  4. Launch File Sorter - it will detect restored data

- **Selective Restore:**
  - Restore only index: Copy `index.json`
  - Restore only versions: Copy `versions/` directory
  - Restore only config: Copy `config.json`

### Export/Import Functionality

- **Export Format:**
  - **JSON format only** for all exports
  - Export index, versions, exceptions, config
  - Structured JSON format matching internal data structures

- **Export Index:**
  - Export indexed file list to JSON
  - Useful for external analysis
  - Command: Available in settings menu
  - Exports complete index structure

- **Import Index:**
  - Import previously exported index JSON
  - Useful for migrating between systems
  - Validates imported data structure
  - Merges with existing index if needed

- **Export Configuration:**
  - Export config (without API keys) for sharing
  - Template for other users
  - Command: Available in settings menu

- **Export/Import .file_sorter Directory:**
  - **Primary method:** Copy entire `.file_sorter/` directory
  - Contains all logic and data:
    - Index data
    - Version history
    - Configuration
    - Exceptions
    - Checkpoints
  - User can copy directory to backup location or another system
  - On import, copy directory to target location
  - Tool detects and uses existing `.file_sorter/` directory

## Data Migration

### Version Migration

- **Config Format Migration:**
  - Automatic migration from old config formats
  - Validates and updates config structure
  - Preserves user settings

- **Index Format Migration:**
  - Automatic migration from old index formats
  - Updates index structure to current version
  - Preserves all indexed data

- **Version History Migration:**
  - Migrates old version format to new format
  - Preserves rollback capability
  - Validates version integrity

### Upgrade Path

- **Automatic Upgrade:**
  - On launch, checks for data format updates
  - Automatically migrates if needed
  - Creates backup before migration

- **Manual Upgrade:**
  - User can trigger migration manually
  - Shows migration preview
  - Requires confirmation before proceeding

## Release Process

### Version Numbering

- **Semantic Versioning:**
  - Format: MAJOR.MINOR.PATCH (e.g., 1.2.3)
  - MAJOR: Breaking changes
  - MINOR: New features, backward compatible
  - PATCH: Bug fixes, backward compatible

### Release Checklist

- **Pre-Release:**
  - All tests passing
  - Code quality checks passing
  - Security scans clean
  - Documentation updated
  - Changelog updated
  - Version number updated

- **Release Steps:**
  1. Create release branch
  2. Update version in `pyproject.toml` and `__init__.py`
  3. Update CHANGELOG.md
  4. Run full test suite
  5. Create GitHub release
  6. Build and publish to PyPI
  7. Tag release in git
  8. Merge to main branch

### Changelog Management

- **CHANGELOG.md Structure:**
  - Reverse chronological order (newest first)
  - Sections: Added, Changed, Deprecated, Removed, Fixed, Security
  - Links to issues/PRs
  - Migration notes for breaking changes

- **Changelog Format:**
```markdown
## [1.2.0] - 2024-01-15

### Added
- New feature X
- Support for Y

### Changed
- Improved performance of Z

### Fixed
- Bug fix A
- Bug fix B
```

## Contributing Guidelines

### Development Workflow

- **Fork and Clone:**
  1. Fork repository on GitHub
  2. Clone your fork locally
  3. Create feature branch: `git checkout -b feature/your-feature`

- **Development:**
  1. Make changes
  2. Write/update tests
  3. Run tests: `pytest`
  4. Run linting: `ruff check src/`
  5. Format code: `black src/`
  6. Check types: `mypy src/`

- **Commit:**
  1. Write clear commit messages
  2. Follow conventional commits format
  3. Reference issues in commit messages

- **Pull Request:**
  1. Push to your fork
  2. Create pull request
  3. Fill out PR template
  4. Wait for code review
  5. Address review comments
  6. Merge after approval

### Code Style

- **Python Style Guide:**
  - Follow PEP 8
  - Use Black for formatting (88 char line length)
  - Use type hints where possible
  - Write docstrings for all public functions

- **Naming Conventions:**
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Private: `_leading_underscore`

### Testing Requirements

- **Test Coverage:**
  - Minimum 80% code coverage
  - Critical paths: 100% coverage
  - All new features must have tests

- **Test Types:**
  - Unit tests for individual functions
  - Integration tests for workflows
  - TUI tests for user interactions

## Security Audit Checklist

### Pre-Release Security Checks

- **Code Security:**
  - No hardcoded secrets or API keys
  - Input validation on all user inputs
  - Path traversal protection
  - SQL injection protection (if using database)
  - XSS protection (if applicable)

- **Dependency Security:**
  - All dependencies up to date
  - No known vulnerabilities (check with `pip audit`)
  - Review dependency licenses

- **File Operations Security:**
  - Permission checks before file operations
  - Path validation (no directory traversal)
  - Atomic operations to prevent race conditions
  - Backup before destructive operations

- **Privacy Security:**
  - No data leakage in logs
  - API keys stored securely
  - No telemetry or tracking
  - Clear privacy warnings

### Security Best Practices

- **Secure Defaults:**
  - Least privilege principle
  - Fail-safe defaults
  - Defense in depth

- **Error Handling:**
  - No sensitive information in error messages
  - Proper error logging
  - Graceful degradation

## Disaster Recovery

### Data Loss Prevention

- **Automatic Backups:**
  - Version snapshots before every change
  - Checkpoint saves during indexing
  - Config backup on changes

- **Recovery Procedures:**
  - Restore from version snapshot
  - Resume from checkpoint
  - Rebuild index if corrupted

### Corruption Detection

- **Index Validation:**
  - Checksum verification
  - Structure validation
  - File existence verification

- **Version Validation:**
  - Version file integrity checks
  - Timestamp validation
  - Structure validation

### Recovery Tools

- **Index Repair:**
  - Detect corrupted index files
  - Attempt automatic repair
  - Rebuild index if repair fails

- **Version Repair:**
  - Validate version files
  - Repair corrupted versions
  - Recover missing versions from backups

## Known Limitations

### Current Limitations

- **File System:**
  - Works with local file systems only
  - Network drives may have performance issues
  - Symlinks are followed (may cause issues)

- **Large Directories:**
  - Very large directories (>100,000 files) may take significant time
  - Memory usage scales with file count
  - Consider using smaller batch sizes

- **File Types:**
  - Some exotic file types may not be recognized
  - Metadata extraction limited to common formats
  - Binary files: type detection only

- **LLM Integration:**
  - Requires API key for cloud LLMs
  - Local LLM (Ollama) requires separate installation
  - Rate limits may apply for cloud LLMs

### Platform Limitations

- **Windows:**
  - Path length limitations (260 chars)
  - File permission differences
  - Case-insensitive file system considerations

- **Linux/MacOS:**
  - Symbolic link handling
  - Permission system differences
  - Case-sensitive file system considerations

## Future Roadmap

### Planned Features (v1.x)

- **Enhanced Filtering:**
  - Advanced file filtering options
  - Custom filter rules
  - Saved filter presets

- **Batch Operations:**
  - Bulk file operations
  - Operation templates
  - Scheduled operations

- **Export/Import:**
  - Export organization plans
  - Import organization templates
  - Share configurations

### Future Considerations (v2.x)

- **Plugin System:**
  - Custom analyzers
  - Custom LLM providers
  - Custom file operations

- **Cloud Integration:**
  - Optional cloud backup
  - Sync between devices
  - Remote indexing

- **Advanced Analytics:**
  - File usage statistics
  - Organization suggestions based on usage
  - Duplicate file detection

## Accessibility Features

### Keyboard Navigation

- **Full Keyboard Support:**
  - All functions accessible via keyboard
  - No mouse required
  - Tab navigation between elements

- **Screen Reader Support:**
  - ARIA labels for all UI elements
  - Descriptive text for all actions
  - Status announcements

### Visual Accessibility

- **Color Contrast:**
  - WCAG AA compliant color contrast
  - Color-blind friendly color schemes
  - High contrast mode option

- **Text Scaling:**
  - Adjustable font sizes
  - Zoom functionality
  - Readable fonts

## Performance Benchmarks

### Target Performance Metrics

- **Indexing Speed:**
  - Small directory (<1000 files): <10 seconds
  - Medium directory (1000-10000 files): <5 minutes
  - Large directory (10000+ files): <30 minutes

- **Memory Usage:**
  - Base memory: <100 MB
  - During indexing: <500 MB (for 10000 files)
  - Peak memory: <1 GB

- **LLM Response Time:**
  - Local LLM (Ollama): <30 seconds
  - Cloud LLM: <10 seconds (network dependent)

### Optimization Goals

- **Indexing:**
  - Process 100+ files per second
  - Batch processing overhead: <5%
  - Checkpoint overhead: <1%

- **File Operations:**
  - Move operation: <100ms per file
  - Rename operation: <50ms per file
  - Directory creation: <10ms per directory

## API Documentation Structure

### Core Module APIs

- **Indexer API (`core/indexer.py`):**
  - `index_directory(path: str) -> IndexResult`
  - `resume_indexing(checkpoint_path: str) -> IndexResult`
  - `get_index_status() -> IndexStatus`

- **Analyzer API (`core/analyzer.py`):**
  - `analyze_file(file_path: str) -> FileAnalysis`
  - `analyze_batch(file_paths: List[str]) -> List[FileAnalysis]`
  - `get_file_type(file_path: str) -> FileType`

- **LLM Client API (`core/llm_client.py`):**
  - `analyze_structure(index: Index, options: LLMOptions) -> LLMRecommendations`
  - `send_request(payload: dict, provider: str) -> dict`
  - `validate_provider(provider: str) -> bool`

- **Version Manager API (`core/version_manager.py`):**
  - `create_version(description: str) -> Version`
  - `rollback_to_version(version_id: int) -> RollbackResult`
  - `get_version_history() -> List[Version]`
  - `selective_rollback(version_id: int, files: List[str]) -> RollbackResult`

- **File Operations API (`core/file_operations.py`):**
  - `move_file(source: str, destination: str) -> OperationResult`
  - `rename_file(file_path: str, new_name: str) -> OperationResult`
  - `create_directory(path: str) -> OperationResult`
  - `execute_operations(operations: List[Operation]) -> BatchResult`

### TUI Component APIs

- **Screen Base Class (`tui/screens/base.py`):**
  - `on_mount()` - Called when screen is mounted
  - `on_unmount()` - Called when screen is unmounted
  - `handle_key(key: Key) -> bool` - Handle keyboard input

- **Main Screen API (`tui/screens/main_screen.py`):**
  - `refresh_file_table()` - Refresh file table display
  - `update_status_header()` - Update status information
  - `block_functions()` - Block unavailable functions
  - `unblock_functions()` - Unblock all functions

- **Indexing Screen API (`tui/screens/indexing.py`):**
  - `start_indexing()` - Start indexing process
  - `pause_indexing()` - Pause indexing
  - `resume_indexing()` - Resume from checkpoint
  - `update_progress(progress: ProgressInfo)` - Update progress display

## Extension Points

### Custom Analyzers

- **Plugin Interface:**
  - Implement `FileAnalyzer` interface
  - Register analyzer in config
  - Custom analyzers run after default analysis

- **Example Use Case:**
  - Custom metadata extraction
  - Domain-specific file analysis
  - Integration with external tools

### Custom LLM Providers

- **Provider Interface:**
  - Implement `LLMProvider` interface
  - Register provider in config
  - Custom providers follow same privacy controls

- **Example Use Case:**
  - Self-hosted LLM servers
  - Custom API endpoints
  - Specialized models

## Troubleshooting Guide

### Common Issues

- **Indexing Issues:**
  - Problem: Indexing hangs or freezes
  - Solution: Check disk space, reduce thread_count, check file permissions
  
  - Problem: Checkpoint corruption
  - Solution: Delete checkpoint file, restart indexing
  
  - Problem: Memory usage too high
  - Solution: Reduce batch_size, reduce thread_count

- **LLM Issues:**
  - Problem: API timeout
  - Solution: Check network connection, increase timeout, use local LLM
  
  - Problem: Rate limit exceeded
  - Solution: Wait and retry, use different provider, reduce request size
  
  - Problem: Invalid API key
  - Solution: Verify API key in config, check provider settings

- **File Operation Issues:**
  - Problem: Permission denied
  - Solution: Check file permissions, run with appropriate privileges
  
  - Problem: Disk full
  - Solution: Free up disk space, check available space before operations
  
  - Problem: File locked
  - Solution: Close applications using files, check for file locks

### Debug Mode

- **Enable Debug Mode:**
  - Command line: `file-sorter --verbose`
  - Config: `"debug": true`
  - Environment: `FILE_SORTER_LOG_LEVEL=DEBUG`

- **Debug Information:**
  - Detailed operation logs
  - Performance metrics
  - LLM request/response (filtered for privacy)
  - File operation details

### Log Analysis

- **Log Locations:**
  - Application logs: `.file_sorter/logs/application.log`
  - Error logs: `.file_sorter/logs/errors.log`
  - Debug logs: `.file_sorter/logs/debug.log`

- **Log Format:**
  - Structured JSON format
  - Timestamp, level, message, context
  - Searchable and parseable

## Maintenance and Updates

### Update Process

- **Checking for Updates:**
  - Manual check: `file-sorter --check-updates`
  - Automatic check: Configurable in settings
  - GitHub releases: Check releases page

- **Updating:**
  - Via pip: `pip install --upgrade file-sorter`
  - Via install script: Re-run install script
  - Manual: Download and install new version

### Data Compatibility

- **Backward Compatibility:**
  - Old index formats automatically migrated
  - Old config formats automatically migrated
  - Version history preserved across updates

- **Breaking Changes:**
  - Documented in CHANGELOG.md
  - Migration guides provided
  - Deprecation warnings before removal

## Support and Community

### Getting Help

- **Documentation:**
  - Full documentation: [docs/](docs/)
  - README.md for quick start
  - FAQ section

- **Community Support:**
  - GitHub Discussions for questions
  - GitHub Issues for bug reports
  - GitHub Discussions for feature requests

### Reporting Issues

- **Bug Report Template:**
  - Description of issue
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - System information
  - Log files (if applicable)

- **Feature Request Template:**
  - Description of feature
  - Use case
  - Proposed implementation
  - Alternatives considered

## Legal and Licensing

### License

- **MIT License:**
  - Permissive open source license
  - Allows commercial use
  - Requires attribution
  - See LICENSE file for details

### Third-Party Licenses

- **Dependencies:**
  - All dependencies listed in requirements.txt
  - License compatibility verified
  - Attribution in documentation

### Privacy Policy

- **Data Collection:**
  - No data collection
  - No telemetry
  - No analytics
  - All processing local

- **User Data:**
  - User owns all data
  - Data stored locally only
  - User can delete all data
  - No data sharing

---

## Development Plan - Step by Step Implementation

This section provides a detailed step-by-step development plan. Each step is **independent and testable**. After completing each step, you can manually test the functionality before proceeding to the next step.

### Development Principles

- **Each step is testable:** After each step, you can run the program and test the new functionality
- **Incremental development:** Each step builds on previous steps
- **Clear testing instructions:** Each step includes manual testing instructions
- **Working state:** After each step, the program should be in a working state (even if incomplete)

---

## Phase 1: Project Foundation

### Step 1.1: Project Structure and Basic Setup

**Goal:** Create basic project structure and ensure Python environment works

**Tasks:**
1. Create project directory structure:
   ```
   file_sorter/
   ├── src/
   │   └── file_sorter/
   │       ├── __init__.py
   │       └── main.py
   ├── tests/
   │   └── __init__.py
   ├── requirements.txt
   ├── .gitignore
   ├── README.md
   └── setup.py
   ```

2. Create `requirements.txt` with minimal dependencies:
   ```
   textual>=0.50.0
   rich>=13.0.0
   ```

3. Create basic `setup.py`:
   - Package name: `file-sorter`
   - Entry point: `file-sorter` command → `file_sorter.main:main`

4. Create `.gitignore`:
   ```
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .Python
   .file_sorter/
   *.egg-info/
   dist/
   build/
   .venv/
   venv/
   ```

5. Create basic `main.py`:
   ```python
   def main():
       print("File Sorter TUI - Starting...")
       print("Project structure OK!")
   
   if __name__ == "__main__":
       main()
   ```

**Testing Instructions:**
1. Install in development mode: `pip install -e .`
2. Run: `file-sorter`
3. **Expected:** Should print "File Sorter TUI - Starting..." and "Project structure OK!"
4. **Verify:** Project structure exists, no errors

**Success Criteria:**
- ✅ Project structure created
- ✅ Can install package with `pip install -e .`
- ✅ Can run `file-sorter` command
- ✅ No errors

---

### Step 1.2: Configuration System

**Goal:** Create configuration system that creates `.file_sorter/config.json` in working directory

**Tasks:**
1. Create `src/file_sorter/utils/config.py`:
   - Function to find/create `.file_sorter/` directory in current working directory
   - Function to load/create `config.json` with defaults
   - Default config structure:
     ```json
     {
       "language": "en",
       "llm_provider": "ollama",
       "llm_model": "llama3",
       "llm_api_key": "",
       "batch_size": 100,
       "thread_count": 4,
       "max_file_size_for_preview": 10485760
     }
     ```

2. Update `main.py` to initialize config:
   - Check/create `.file_sorter/` directory
   - Load/create config.json
   - Print config location

**Testing Instructions:**
1. Run: `file-sorter`
2. **Expected:** Should create `.file_sorter/` directory in current directory
3. **Expected:** Should create `config.json` with default values
4. Check: `ls -la .file_sorter/` (should show config.json)
5. Check: `cat .file_sorter/config.json` (should show default config)
6. Change directory: `cd subdirectory && file-sorter`
7. **Expected:** Should create new `.file_sorter/` in subdirectory

**Success Criteria:**
- ✅ `.file_sorter/` directory created in working directory
- ✅ `config.json` created with defaults
- ✅ Config can be loaded
- ✅ Each directory gets its own `.file_sorter/`

---

### Step 1.3: Directory Selection Logic

**Goal:** Implement logic to check parent directories for existing `.file_sorter/`

**Tasks:**
1. Add function to `utils/config.py`:
   - `find_parent_file_sorter()` - walks up directory tree looking for `.file_sorter/`
   - Returns path if found, None otherwise

2. Update `main.py`:
   - If in subdirectory, check for parent `.file_sorter/`
   - If found, print message: "Found .file_sorter in parent directory: {path}"
   - Ask user: "Use parent's .file_sorter? (y/n)" (for now, just print)

**Testing Instructions:**
1. Create test structure:
   ```
   test_dir/
   ├── .file_sorter/
   │   └── config.json
   └── subdir/
   ```
2. Run from `test_dir/`: `file-sorter`
3. **Expected:** Uses `test_dir/.file_sorter/`
4. Run from `test_dir/subdir/`: `file-sorter`
5. **Expected:** Detects parent `.file_sorter/` and prints message

**Success Criteria:**
- ✅ Can detect parent `.file_sorter/`
- ✅ Prints appropriate message
- ✅ Works correctly in nested directories

---

## Phase 2: Translation System

### Step 2.1: Basic Translation System

**Goal:** Create translation system with JSON files (en, lv, ru), English default

**Tasks:**
1. Create `src/file_sorter/i18n/` directory:
   ```
   i18n/
   ├── __init__.py
   ├── translations.py
   ├── en.json
   ├── lv.json
   └── ru.json
   ```

2. Create `en.json` (default):
   ```json
   {
     "app": {
       "title": "File Sorter",
       "welcome": "Welcome to File Sorter"
     },
     "main_menu": {
       "title": "Main Menu",
       "start_indexing": "Start Indexing",
       "settings": "Settings",
       "help": "Help",
       "exit": "Exit"
     }
   }
   ```

3. Create `lv.json` and `ru.json` with translations

4. Create `translations.py`:
   - Load JSON files
   - Function `t(key, lang="en")` to get translation
   - Function `set_language(lang)` to change language
   - Load language from config

5. Update `main.py`:
   - Load translations
   - Print welcome message using translations
   - Print menu options using translations

**Testing Instructions:**
1. Run: `file-sorter`
2. **Expected:** All text in English (default)
3. Change config: `"language": "lv"` in config.json
4. Run: `file-sorter`
5. **Expected:** All text in Latvian
6. Change config: `"language": "ru"`
7. Run: `file-sorter`
8. **Expected:** All text in Russian

**Success Criteria:**
- ✅ Translation files load correctly
- ✅ Default language is English
- ✅ Can switch languages via config
- ✅ All UI text uses translations

---

## Phase 3: Basic TUI

### Step 3.1: Basic Textual Application

**Goal:** Create basic Textual TUI application that starts and shows welcome screen

**Tasks:**
1. Update `requirements.txt`:
   ```
   textual>=0.50.0
   rich>=13.0.0
   ```

2. Create `src/file_sorter/tui/app.py`:
   - Basic Textual App class
   - Welcome screen with title
   - Exit on 'q' key

3. Update `main.py`:
   - Import and run Textual app
   - Load language from config
   - Show welcome message

**Testing Instructions:**
1. Run: `file-sorter`
2. **Expected:** TUI window opens
3. **Expected:** Shows welcome message
4. Press 'q' to quit
5. **Expected:** Application exits cleanly

**Success Criteria:**
- ✅ TUI application starts
- ✅ Shows welcome screen
- ✅ Can exit with 'q'
- ✅ No errors

---

### Step 3.2: Main Screen Layout (Top-like UI)

**Goal:** Create main screen with header (top section) and content area (bottom section)

**Tasks:**
1. Create `src/file_sorter/tui/screens/main_screen.py`:
   - Header widget (top section):
     - Title: "File Sorter"
     - Status: "Indexing: Not Started"
     - System info placeholder
   - Content area (bottom section):
     - Placeholder text: "File list will appear here"
   - Layout: Header takes ~20% height, content takes ~80%

2. Update `app.py`:
   - Set main_screen as initial screen

**Testing Instructions:**
1. Run: `file-sorter`
2. **Expected:** Main screen shows with header and content area
3. **Expected:** Header shows title and status
4. **Expected:** Content area shows placeholder
5. **Expected:** Layout looks like "top" command (header on top, content below)

**Success Criteria:**
- ✅ Main screen displays correctly
- ✅ Layout matches "top" style
- ✅ Header and content areas visible
- ✅ No layout errors

---

### Step 3.3: Language Selection Screen

**Goal:** Add language selection screen accessible from main menu

**Tasks:**
1. Create `src/file_sorter/tui/screens/language_select.py`:
   - List of languages: English, Latvian, Russian
   - Can select language with arrow keys
   - Confirm with Enter
   - Updates config and reloads translations

2. Update main screen:
   - Add menu option: "Change Language" (key 'l')
   - Opens language selection screen

**Testing Instructions:**
1. Run: `file-sorter`
2. Press 'l' for language selection
3. **Expected:** Language selection screen opens
4. Use arrow keys to select language
5. Press Enter to confirm
6. **Expected:** Returns to main screen
7. **Expected:** All text in selected language
8. Check config.json: `"language"` should be updated

**Success Criteria:**
- ✅ Language selection screen works
- ✅ Can select language
- ✅ Language changes immediately
- ✅ Config updated correctly

---

## Phase 4: Indexing System

### Step 4.1: Basic File Indexer (No Analysis)

**Goal:** Create basic file indexer that lists all files recursively

**Tasks:**
1. Create `src/file_sorter/core/indexer.py`:
   - Function `index_directory(path)`:
     - Recursively walks directory
     - Collects file paths, names, sizes, modification dates
     - Returns list of file info dictionaries
   - Basic structure (no analysis yet):
     ```python
     {
       "path": "relative/path/to/file.txt",
       "name": "file.txt",
       "size": 1024,
       "modified": "2024-01-01T10:00:00",
       "is_directory": False
     }
     ```

2. Create `src/file_sorter/storage/index_storage.py`:
   - Function `save_index(index_data, path)`:
     - Saves to `.file_sorter/index.json`
     - Includes `indexed_at` timestamp
   - Function `load_index(path)`:
     - Loads index from `.file_sorter/index.json`
     - Returns index data or None

3. Update main screen:
   - Add "Start Indexing" button/menu option
   - When clicked, runs indexer
   - Shows progress: "Indexing... X files found"
   - Saves index when done

**Testing Instructions:**
1. Create test directory with files:
   ```
   test_files/
   ├── file1.txt
   ├── file2.jpg
   └── subdir/
       └── file3.pdf
   ```
2. Run: `file-sorter` from test_files directory
3. Press key to start indexing (e.g., 'i')
4. **Expected:** Shows "Indexing... X files found"
5. **Expected:** After completion, shows "Indexing complete: 3 files"
6. Check: `cat .file_sorter/index.json`
7. **Expected:** JSON file contains all 3 files with paths, sizes, dates

**Success Criteria:**
- ✅ Can index directory recursively
- ✅ Collects file paths, names, sizes, dates
- ✅ Saves index to JSON
- ✅ Can load index from JSON
- ✅ Shows progress during indexing

---

### Step 4.2: Indexing Status Check

**Goal:** Check indexing status on startup and block functions if not indexed

**Tasks:**
1. Update `main_screen.py`:
   - On startup, check if `index.json` exists
   - Check `indexed_at` timestamp
   - If no index or incomplete:
     - Show status: "Indexing: Not Started" or "Indexing: Incomplete"
     - Block functions (gray out menu options)
     - Show message: "Please start indexing first"
   - If indexed:
     - Show status: "Indexing: Complete (Last: {timestamp})"
     - Enable all functions

2. Add visual indicators:
   - Disabled menu options appear grayed out
   - Enabled options appear normal

**Testing Instructions:**
1. Run: `file-sorter` in new directory
2. **Expected:** Status shows "Indexing: Not Started"
3. **Expected:** Most menu options grayed out/disabled
4. **Expected:** Only "Start Indexing" and "Settings" available
5. Start indexing and complete it
6. Restart: `file-sorter`
7. **Expected:** Status shows "Indexing: Complete (Last: {date})"
8. **Expected:** All menu options enabled

**Success Criteria:**
- ✅ Checks index status on startup
- ✅ Shows correct status
- ✅ Blocks functions when not indexed
- ✅ Enables functions when indexed
- ✅ Visual indicators work

---

### Step 4.3: Batch Processing and Progress

**Goal:** Implement batch processing for large file counts (10000+)

**Tasks:**
1. Update `indexer.py`:
   - Process files in batches (configurable, default 100)
   - After each batch, save checkpoint
   - Show progress: "Processing batch X/Y (Z files processed)"
   - Yield progress updates

2. Create `src/file_sorter/storage/checkpoint_manager.py`:
   - Function `save_checkpoint(progress_data, path)`:
     - Saves to `.file_sorter/index_checkpoint.json`
     - Includes: processed files list, batch number, total files
   - Function `load_checkpoint(path)`:
     - Loads checkpoint
     - Returns checkpoint data or None

3. Update main screen:
   - Show progress during indexing
   - Update every batch completion

**Testing Instructions:**
1. Create test directory with many files (or use existing large directory)
2. Run: `file-sorter`
3. Start indexing
4. **Expected:** Shows progress: "Processing batch 1/10 (100 files processed)"
5. **Expected:** Progress updates as batches complete
6. Interrupt indexing (Ctrl+C)
7. Check: `cat .file_sorter/index_checkpoint.json`
8. **Expected:** Checkpoint file exists with progress data
9. Restart: `file-sorter`
10. **Expected:** Offers to resume from checkpoint

**Success Criteria:**
- ✅ Processes files in batches
- ✅ Shows progress updates
- ✅ Saves checkpoint after each batch
- ✅ Can detect interrupted indexing
- ✅ Checkpoint file created correctly

---

### Step 4.4: Resume from Checkpoint

**Goal:** Allow resuming indexing from checkpoint

**Tasks:**
1. Update `indexer.py`:
   - Check for checkpoint on startup
   - If checkpoint exists:
     - Load processed files list
     - Skip already processed files
     - Continue from last batch
   - Show resume option in UI

2. Update main screen:
   - If checkpoint exists, show: "Resume indexing? (y/n)"
   - If yes, resume from checkpoint
   - If no, start fresh (delete checkpoint)

**Testing Instructions:**
1. Start indexing in large directory
2. Interrupt indexing (Ctrl+C)
3. Restart: `file-sorter`
4. **Expected:** Shows "Resume indexing? (y/n)"
5. Press 'y'
6. **Expected:** Resumes from checkpoint
7. **Expected:** Skips already processed files
8. **Expected:** Completes indexing
9. **Expected:** Checkpoint deleted when complete

**Success Criteria:**
- ✅ Detects checkpoint on startup
- ✅ Can resume from checkpoint
- ✅ Skips already processed files
- ✅ Completes indexing after resume
- ✅ Checkpoint deleted on completion

---

### Step 4.5: File Analysis (Surface-level)

**Goal:** Add surface-level file analysis (magic numbers, metadata, no full content)

**Tasks:**
1. Create `src/file_sorter/core/analyzer.py`:
   - Function `analyze_file(file_path)`:
     - Detects file type using magic numbers (python-magic or filetype)
     - Extracts basic metadata (size, date)
     - For text files: reads first 512 bytes only
     - For images: extracts EXIF if available (Pillow)
     - For audio: extracts ID3 tags if available (mutagen)
     - Returns analysis dictionary

2. Update `indexer.py`:
   - Call analyzer for each file
   - Add analysis results to index
   - Skip content preview for large files (>10MB)

3. Update index structure:
   ```json
   {
     "file_type": "text/plain",
     "mime_type": "text/plain",
     "magic_number": "ASCII text",
     "content_preview": "First 512 bytes...",
     "metadata": {}
   }
   ```

**Testing Instructions:**
1. Create test files:
   - `test.txt` (text file)
   - `test.jpg` (image file)
   - `test.mp3` (audio file, if available)
2. Run indexing
3. Check: `cat .file_sorter/index.json`
4. **Expected:** Each file has `file_type`, `mime_type`, `magic_number`
5. **Expected:** Text file has `content_preview` (first 512 bytes)
6. **Expected:** Image file has EXIF metadata (if available)
7. **Expected:** Large files (>10MB) don't have content_preview

**Success Criteria:**
- ✅ Detects file types correctly
- ✅ Extracts metadata
- ✅ Reads only first 512 bytes for text files
- ✅ Skips content for large files
- ✅ No full file content reading

---

### Step 4.6: Parallel Processing

**Goal:** Implement parallel processing for faster indexing

**Tasks:**
1. Update `indexer.py`:
   - Use `concurrent.futures.ThreadPoolExecutor`
   - Process files in parallel (configurable thread count, default 4)
   - Process batches in parallel
   - Thread-safe progress tracking

2. Update config:
   - Add `thread_count` setting (default 4)

**Testing Instructions:**
1. Run indexing in directory with many files
2. **Expected:** Multiple files processed simultaneously
3. **Expected:** Faster than sequential processing
4. **Expected:** Progress updates correctly
5. Check CPU usage: should use multiple cores
6. Test with different `thread_count` values (1, 4, 8)

**Success Criteria:**
- ✅ Processes files in parallel
- ✅ Faster than sequential
- ✅ Thread-safe progress tracking
- ✅ Configurable thread count
- ✅ No race conditions

---

### Step 4.7: Incremental Indexing

**Goal:** Only re-index changed files on subsequent runs

**Tasks:**
1. Update `indexer.py`:
   - Save file hash sums in index
   - On next run:
     - Compare modification dates first (fast)
     - If date changed, compare hash
     - Only re-index changed/new files
     - Remove deleted files from index

2. Update index structure:
   ```json
   {
     "file_hash": "abc123...",
     "indexed_at": "2024-01-01T10:00:00",
     "modified_at": "2024-01-01T09:00:00"
   }
   ```

**Testing Instructions:**
1. Run indexing (creates initial index)
2. Modify one file
3. Delete one file
4. Add one new file
5. Run indexing again
6. **Expected:** Only processes 3 files (1 modified, 1 new, detects 1 deleted)
7. **Expected:** Much faster than full re-indexing
8. Check index: should have updated data for changed files
9. Check index: deleted file should be removed

**Success Criteria:**
- ✅ Detects changed files by date
- ✅ Verifies with hash if needed
- ✅ Only re-indexes changed/new files
- ✅ Removes deleted files from index
- ✅ Much faster than full indexing

---

## Phase 5: TUI Indexing Screen

### Step 5.1: Real-time Indexing Screen

**Goal:** Create indexing screen with real-time progress display (top-like UI)

**Tasks:**
1. Create `src/file_sorter/tui/screens/indexing.py`:
   - **Top section (header):**
     - Progress bar
     - Files processed / total files
     - Processing speed (files/s)
     - Estimated remaining time
     - Current batch / total batches
   - **Bottom section:**
     - Live file processing table
     - Shows files currently being processed
     - Updates in real-time

2. Update `main.py`:
   - Navigate to indexing screen when "Start Indexing" clicked
   - Run indexer in background
   - Update UI with progress

**Testing Instructions:**
1. Run: `file-sorter`
2. Start indexing
3. **Expected:** Indexing screen opens
4. **Expected:** Header shows progress bar, stats
5. **Expected:** Bottom section shows files being processed
6. **Expected:** Updates in real-time (every 100-500ms)
7. **Expected:** Can see files appearing in table as processed
8. **Expected:** When complete, transitions to main screen

**Success Criteria:**
- ✅ Indexing screen displays correctly
- ✅ Shows real-time progress
- ✅ Updates frequently
- ✅ Shows files being processed
- ✅ Transitions to main screen when complete

---

### Step 5.2: Pause/Resume Indexing

**Goal:** Allow pausing and resuming indexing

**Tasks:**
1. Update `indexing.py`:
   - Add pause button/key ('p')
   - When paused:
     - Saves checkpoint immediately
     - Shows "Paused" status
     - Can resume ('r') or cancel ('c')

2. Update `indexer.py`:
   - Check for pause flag periodically
   - Save checkpoint when paused
   - Can resume from pause point

**Testing Instructions:**
1. Start indexing
2. Press 'p' to pause
3. **Expected:** Indexing pauses
4. **Expected:** Status shows "Paused"
5. **Expected:** Checkpoint saved
6. Press 'r' to resume
7. **Expected:** Resumes from pause point
8. **Expected:** Continues processing
9. Press 'c' to cancel
10. **Expected:** Cancels indexing, returns to main screen

**Success Criteria:**
- ✅ Can pause indexing
- ✅ Saves checkpoint when paused
- ✅ Can resume from pause
- ✅ Can cancel indexing
- ✅ State saved correctly

---

## Phase 6: File Table Display

### Step 6.1: Basic File Table

**Goal:** Display indexed files in table format on main screen

**Tasks:**
1. Create `src/file_sorter/tui/widgets/file_table.py`:
   - DataTable widget
   - Columns: Name, Path, Type, Size, Modified
   - Loads data from index.json
   - Displays all indexed files

2. Update `main_screen.py`:
   - Replace placeholder with file table
   - Load index and display files
   - Show "No files indexed" if index empty

**Testing Instructions:**
1. Index some files
2. Return to main screen
3. **Expected:** File table shows all indexed files
4. **Expected:** Columns: Name, Path, Type, Size, Modified
5. **Expected:** Can scroll through files
6. **Expected:** Data matches index.json

**Success Criteria:**
- ✅ File table displays correctly
- ✅ Shows all indexed files
- ✅ Columns correct
- ✅ Can scroll
- ✅ Data accurate

---

### Step 6.2: Table Virtualization (Large Files)

**Goal:** Handle large file counts (10000+) efficiently with virtualization

**Tasks:**
1. Update `file_table.py`:
   - Use Textual's built-in virtualization
   - Only render visible rows
   - Lazy loading as user scrolls
   - Efficient memory usage

2. Test with large dataset:
   - Create test directory with 10000+ files (or use existing)
   - Index all files
   - Display in table
   - **Expected:** No lag, smooth scrolling
   - **Expected:** Low memory usage

**Testing Instructions:**
1. Index large directory (10000+ files)
2. Open main screen
3. **Expected:** Table loads quickly
4. **Expected:** Can scroll smoothly
5. **Expected:** No freezing or lag
6. Check memory usage: should be reasonable
7. **Expected:** Only visible rows rendered

**Success Criteria:**
- ✅ Handles 10000+ files efficiently
- ✅ Smooth scrolling
- ✅ Low memory usage
- ✅ No freezing
- ✅ Virtualization works

---

### Step 6.3: Sortable and Filterable Table

**Goal:** Add sorting and filtering to file table

**Tasks:**
1. Update `file_table.py`:
   - Click column header to sort
   - Sort by: Name, Size, Type, Modified
   - Add filter input
   - Filter by: name, type, path

2. Add keyboard shortcuts:
   - 's' - sort menu
   - 'f' - focus filter
   - Arrow keys - navigate rows

**Testing Instructions:**
1. Display file table
2. Click "Name" column header
3. **Expected:** Sorts by name (ascending)
4. Click again
5. **Expected:** Sorts by name (descending)
6. Press 'f' to focus filter
7. Type "txt"
8. **Expected:** Shows only .txt files
9. Clear filter
10. **Expected:** Shows all files again

**Success Criteria:**
- ✅ Can sort by columns
- ✅ Sorting works correctly
- ✅ Can filter files
- ✅ Filter updates in real-time
- ✅ Keyboard shortcuts work

---

### Step 6.4: Multi-select Files

**Goal:** Allow selecting multiple files for batch operations

**Tasks:**
1. Update `file_table.py`:
   - Space key toggles selection
   - Ctrl+A selects all visible
   - Ctrl+D deselects all
   - Visual indicator for selected files
   - Show selected count

**Testing Instructions:**
1. Display file table
2. Navigate to file with arrow keys
3. Press Space
4. **Expected:** File selected (highlighted)
5. Navigate to another file
6. Press Space
7. **Expected:** Both files selected
8. Press Ctrl+A
9. **Expected:** All visible files selected
10. Press Ctrl+D
11. **Expected:** All deselected
12. **Expected:** Selected count displayed

**Success Criteria:**
- ✅ Can select multiple files
- ✅ Visual indicators work
- ✅ Keyboard shortcuts work
- ✅ Selected count displayed
- ✅ Selection persists during navigation

---

### Step 6.5: Smart Search

**Goal:** Implement smart search with multi-language support

**Tasks:**
1. Update `file_table.py`:
   - Search input field
   - Search by: name, type, path, content preview
   - Fuzzy matching
   - Multi-language support (handles Latvian, Russian characters)

2. Add search highlighting:
   - Highlight matching text in results

**Testing Instructions:**
1. Display file table
2. Press '/' to focus search
3. Type "txt"
4. **Expected:** Shows files matching "txt"
5. Type "документ" (Russian)
6. **Expected:** Finds files with Russian names
7. Type "faili" (Latvian)
8. **Expected:** Finds files with Latvian names
9. Test fuzzy matching: "txt" should find "text", "document.txt"

**Success Criteria:**
- ✅ Search works correctly
- ✅ Multi-language support
- ✅ Fuzzy matching works
- ✅ Highlights matches
- ✅ Real-time filtering

---

### Step 6.6: Detailed File Info View

**Goal:** Show detailed file information on demand

**Tasks:**
1. Create detail view dialog:
   - Opens when Enter pressed on file
   - Shows: full path, size, type, metadata, content preview
   - Can close with Esc

2. Update `file_table.py`:
   - Enter key opens detail view
   - Shows detailed information

**Testing Instructions:**
1. Display file table
2. Navigate to file
3. Press Enter
4. **Expected:** Detail view opens
5. **Expected:** Shows full file information
6. **Expected:** Shows metadata
7. **Expected:** Shows content preview (if available)
8. Press Esc
9. **Expected:** Closes detail view

**Success Criteria:**
- ✅ Detail view opens correctly
- ✅ Shows complete information
- ✅ Can close detail view
- ✅ Information accurate

---

### Step 6.7: Ignored Files Section

**Goal:** Show ignored files (matching exceptions) in separate section

**Tasks:**
1. Create exceptions system (see Step 7.1)
2. Update `file_table.py`:
   - Add tab/section for "Ignored Files"
   - Show files matching exceptions
   - Visual distinction (grayed out or different color)

**Testing Instructions:**
1. Create exceptions (mark some files/directories as ignored)
2. Index directory
3. Display file table
4. Switch to "Ignored Files" tab
5. **Expected:** Shows ignored files
6. **Expected:** Visual distinction from normal files
7. Switch back to normal files
8. **Expected:** Ignored files not shown

**Success Criteria:**
- ✅ Ignored files section exists
- ✅ Shows correct files
- ✅ Visual distinction
- ✅ Can switch between sections

---

## Phase 7: Exceptions System

### Step 7.1: Exceptions Management

**Goal:** Create system to mark files/directories/extensions as ignored

**Tasks:**
1. Create `src/file_sorter/core/exceptions_manager.py`:
   - Load/save `exceptions.json`
   - Structure:
     ```json
     {
       "directories": ["path/to/dir"],
       "files": ["path/to/file"],
       "extensions": [".pdf", ".docx"],
       "patterns": ["*secret*"]
     }
     ```

2. Create exceptions management screen:
   - Add directory to exceptions
   - Add file to exceptions
   - Add extension to exceptions
   - Add pattern to exceptions
   - Remove exceptions
   - List all exceptions

3. Update indexer:
   - Check exceptions before indexing
   - Skip files matching exceptions

**Testing Instructions:**
1. Open exceptions management
2. Add directory to exceptions
3. **Expected:** Directory added to exceptions.json
4. Add extension ".pdf" to exceptions
5. **Expected:** Extension added
6. Start indexing
7. **Expected:** PDF files skipped
8. **Expected:** Exception directory skipped
9. Check ignored files section
10. **Expected:** Shows skipped files

**Success Criteria:**
- ✅ Can add exceptions
- ✅ Exceptions saved to JSON
- ✅ Indexer skips exceptions
- ✅ Ignored files shown separately
- ✅ Exceptions persist across sessions

---

## Phase 8: Version Management

### Step 8.1: Basic Version System

**Goal:** Create version system that saves directory structure before changes

**Tasks:**
1. Create `src/file_sorter/core/version_manager.py`:
   - Function `create_version(description)`:
     - Saves current directory structure to `versions/vN.json`
     - Includes timestamp, description
     - Only saves structure (paths, names), not file contents
   - Function `list_versions()`:
     - Returns list of all versions
   - Function `get_version(version_num)`:
     - Loads version data

2. Create `src/file_sorter/storage/version_storage.py`:
   - Save/load version files
   - Compress versions (gzip)

3. Update main screen:
   - Show version list
   - Create version before operations

**Testing Instructions:**
1. Index some files
2. Create version: "Initial state"
3. **Expected:** Version created in `versions/v1.json`
4. Check version file
5. **Expected:** Contains directory structure
6. Make some changes (manually, for now)
7. Create version: "After changes"
8. **Expected:** Version v2 created
9. List versions
10. **Expected:** Shows both versions

**Success Criteria:**
- ✅ Can create versions
- ✅ Versions saved correctly
- ✅ Can list versions
- ✅ Can load version data
- ✅ Versions compressed

---

### Step 8.2: Version Optimization

**Goal:** Optimize version storage (incremental, compression)

**Tasks:**
1. Update `version_manager.py`:
   - Incremental storage: only save changes from previous version
   - Gzip compression for version files
   - Smart storage: split large directories if needed

2. Test with large directory:
   - Create version
   - **Expected:** Version file is compressed
   - **Expected:** Only stores changes (if incremental)
   - **Expected:** File size reasonable

**Testing Instructions:**
1. Create version in large directory
2. Check version file size
3. **Expected:** Compressed (smaller than uncompressed)
4. Create second version with small changes
5. **Expected:** Only stores changes (if incremental)
6. **Expected:** File size much smaller

**Success Criteria:**
- ✅ Versions compressed
- ✅ Incremental storage works (if implemented)
- ✅ File sizes reasonable
- ✅ Can still load versions correctly

---

### Step 8.3: Rollback Functionality

**Goal:** Implement rollback to previous version

**Tasks:**
1. Update `version_manager.py`:
   - Function `rollback_to_version(version_num)`:
     - Loads version structure
     - Compares with current structure
     - Creates plan to restore structure
     - Returns operations needed

2. Create rollback preview screen:
   - Shows what will be changed
   - User confirms
   - Executes rollback

3. Update file operations:
   - Use rollback to restore files

**Testing Instructions:**
1. Create version v1
2. Make changes (add/delete/move files)
3. Create version v2
4. Rollback to v1
5. **Expected:** Shows preview of changes
6. Confirm rollback
7. **Expected:** Files restored to v1 state
8. **Expected:** New version v3 created (rollback operation)

**Success Criteria:**
- ✅ Can rollback to version
- ✅ Shows preview before rollback
- ✅ Restores structure correctly
- ✅ Creates new version for rollback
- ✅ Files restored accurately

---

## Phase 9: LLM Integration

### Step 9.1: LLM Client Basic Structure

**Goal:** Create LLM client with support for multiple providers

**Tasks:**
1. Create `src/file_sorter/core/llm_client.py`:
   - Base LLM client class
   - Provider classes: OpenAI, Anthropic, Ollama, Custom
   - Function `send_request(prompt, data)`:
     - Formats request
     - Sends to provider
     - Returns response

2. Update config:
   - LLM provider settings
   - API key storage (encrypted or secure)

3. Create LLM settings screen:
   - Select provider
   - Enter API key
   - Test connection

**Testing Instructions:**
1. Open LLM settings
2. Select provider (e.g., Ollama)
3. Enter API key (if needed)
4. Test connection
5. **Expected:** Connection successful
6. Save settings
7. Check config.json
8. **Expected:** Provider and key saved (key encrypted if possible)

**Success Criteria:**
- ✅ Can select provider
- ✅ Can enter API key
- ✅ Connection test works
- ✅ Settings saved
- ✅ API key stored securely

---

### Step 9.2: LLM Request Preparation

**Goal:** Prepare data to send to LLM (structure, metadata, user instructions)

**Tasks:**
1. Update `llm_client.py`:
   - Function `prepare_request(index_data, options)`:
     - Filters private files (exceptions)
     - Formats data based on options:
       - Structure only
       - Structure + metadata
       - Structure + metadata + previews
     - Adds user instructions
     - Returns JSON payload

2. Create request preview screen:
   - Shows JSON that will be sent
   - User can review
   - User can add custom instructions
   - User confirms before sending

**Testing Instructions:**
1. Index files
2. Open LLM analysis
3. Select data to send (structure only)
4. **Expected:** Shows JSON preview
5. **Expected:** Private files not included
6. Add custom instructions: "Organize by file type"
7. **Expected:** Instructions added to request
8. Review JSON
9. **Expected:** JSON formatted correctly
10. **Expected:** Only selected data included

**Success Criteria:**
- ✅ Prepares request correctly
- ✅ Filters private files
- ✅ Shows JSON preview
- ✅ User can add instructions
- ✅ User can review before sending

---

### Step 9.3: LLM Response Handling

**Goal:** Send request to LLM and handle response

**Tasks:**
1. Update `llm_client.py`:
   - Send request to provider
   - Handle errors (retry, fallback)
   - Parse response
   - Validate response format

2. Create response screen:
   - Shows LLM response
   - Validates format
   - If invalid, request retry
   - Option to save request/response

**Testing Instructions:**
1. Prepare LLM request
2. Send to LLM
3. **Expected:** Shows progress indicator
4. **Expected:** Receives response
5. **Expected:** Response displayed
6. Test with invalid response (mock)
7. **Expected:** Validates format
8. **Expected:** Requests retry if invalid
9. Test save option
10. **Expected:** Request/response saved locally

**Success Criteria:**
- ✅ Sends request correctly
- ✅ Handles errors gracefully
- ✅ Parses response
- ✅ Validates format
- ✅ Can save request/response
- ✅ Can retry on error

---

### Step 9.4: LLM Response Validation and Format

**Goal:** Ensure LLM returns data in correct format

**Tasks:**
1. Update `llm_client.py`:
   - Define expected response format:
     ```json
     {
       "operations": [
         {"type": "move", "source": "...", "destination": "..."},
         {"type": "rename", "source": "...", "destination": "..."},
         {"type": "create_directory", "path": "..."}
       ]
     }
     ```
   - Validate response matches format
   - If invalid, send format instructions to LLM
   - Request retry with clearer instructions

2. Update LLM prompt:
   - Include format requirements
   - Request concise response
   - Request clear instructions

**Testing Instructions:**
1. Send request to LLM
2. **Expected:** Response in correct format
3. Test with mock invalid response
4. **Expected:** Detects invalid format
5. **Expected:** Sends format instructions
6. **Expected:** Requests retry
7. **Expected:** Retry returns valid format

**Success Criteria:**
- ✅ Response format validated
- ✅ Invalid responses detected
- ✅ Format instructions sent
- ✅ Retry works
- ✅ Response format correct

---

## Phase 10: File Operations

### Step 10.1: Basic File Operations

**Goal:** Implement file move, rename, directory creation

**Tasks:**
1. Create `src/file_sorter/core/file_operations.py`:
   - Function `move_file(source, destination)`:
     - Validates paths
     - Moves file
     - Returns success/error
   - Function `rename_file(source, new_name)`:
     - Renames file
     - Returns success/error
   - Function `create_directory(path)`:
     - Creates directory
     - Returns success/error

2. Create operation preview screen:
   - Shows planned operations
   - User confirms
   - Executes operations

**Testing Instructions:**
1. Get LLM recommendations (or create manually)
2. Preview operations
3. **Expected:** Shows list of operations
4. Confirm execution
5. **Expected:** Files moved/renamed
6. **Expected:** Directories created
7. Check file system
8. **Expected:** Changes applied correctly

**Success Criteria:**
- ✅ Can move files
- ✅ Can rename files
- ✅ Can create directories
- ✅ Operations execute correctly
- ✅ Preview works

---

### Step 10.2: Conflict Resolution

**Goal:** Handle file conflicts (already exists, symlinks, hard links)

**Tasks:**
1. Update `file_operations.py`:
   - Check for conflicts before operation
   - Detect: file exists, symlinks, hard links
   - Ask user what to do:
     - File exists: overwrite, skip, rename
     - Symlink: follow, ignore, treat as file
     - Hard link: treat as separate, maintain link, skip

2. Create conflict resolution dialog:
   - Shows conflict details
   - User chooses action
   - Saves preference for future

**Testing Instructions:**
1. Create test scenario:
   - File exists at destination
   - Symlink exists
   - Hard link exists
2. Attempt operation
3. **Expected:** Conflict detected
4. **Expected:** Dialog shows options
5. Choose action
6. **Expected:** Operation proceeds with chosen action
7. Test preference saving
8. **Expected:** Preference saved in config

**Success Criteria:**
- ✅ Detects conflicts
- ✅ Shows options
- ✅ User can choose action
- ✅ Preference saved
- ✅ Operations proceed correctly

---

### Step 10.3: Atomic Operations

**Goal:** Implement transaction-like behavior (all or nothing)

**Tasks:**
1. Update `file_operations.py`:
   - Group operations into transaction
   - Validate all operations before execution
   - Execute all operations
   - If any fails, rollback all
   - Create version before transaction

2. Test rollback:
   - Create transaction with multiple operations
   - Make one operation fail (e.g., permission error)
   - **Expected:** All operations rolled back
   - **Expected:** Previous state restored

**Testing Instructions:**
1. Create version v1
2. Plan multiple operations
3. Execute transaction
4. **Expected:** All operations succeed or all rollback
5. Test with failure:
   - Create operation that will fail
   - Execute transaction
6. **Expected:** All operations rolled back
7. **Expected:** State restored to v1

**Success Criteria:**
- ✅ Operations grouped into transactions
- ✅ All succeed or all rollback
- ✅ Rollback works correctly
- ✅ State consistent
- ✅ Version created before operations

---

### Step 10.4: Permission Handling

**Goal:** Handle files without read permissions

**Tasks:**
1. Update `indexer.py`:
   - Try to access file
   - If permission error, skip file
   - Log skipped files
   - Show in ignored files section

2. Update `file_operations.py`:
   - Check permissions before operations
   - Skip files without permissions
   - Show warning

**Testing Instructions:**
1. Create file without read permission (chmod 000)
2. Run indexing
3. **Expected:** File skipped
4. **Expected:** Logged as skipped
5. **Expected:** Shown in ignored files section
6. Try to operate on file
7. **Expected:** Operation skipped
8. **Expected:** Warning shown

**Success Criteria:**
- ✅ Files without permissions skipped
- ✅ Logged correctly
- ✅ Shown in ignored section
- ✅ Operations skip correctly
- ✅ Warnings shown

---

## Phase 11: Integration and Polish

### Step 11.1: Complete Workflow Integration

**Goal:** Integrate all components into complete workflow

**Tasks:**
1. Connect all screens:
   - Main screen → Indexing → LLM Analysis → Preview → Execution
   - Main screen → Version List → Rollback
   - Main screen → Settings → Language/LLM/Exceptions

2. Test complete workflow:
   - Index files
   - Analyze with LLM
   - Preview changes
   - Execute operations
   - Create version
   - Rollback if needed

**Testing Instructions:**
1. Run complete workflow:
   - Start indexing
   - Wait for completion
   - Analyze with LLM
   - Review recommendations
   - Preview changes
   - Execute operations
   - Verify changes
   - Rollback if needed
2. **Expected:** All steps work correctly
3. **Expected:** Smooth transitions
4. **Expected:** No errors

**Success Criteria:**
- ✅ Complete workflow works
- ✅ All screens connected
- ✅ Transitions smooth
- ✅ No errors
- ✅ State consistent

---

### Step 11.2: Error Handling and Recovery

**Goal:** Add comprehensive error handling

**Tasks:**
1. Add error handling to all components:
   - File operations errors
   - LLM API errors
   - Indexing errors
   - Network errors

2. Create error recovery:
   - Rollback on failure
   - Retry mechanisms
   - User-friendly error messages

**Testing Instructions:**
1. Test error scenarios:
   - File operation fails
   - LLM API fails
   - Network error
   - Disk full
2. **Expected:** Errors handled gracefully
3. **Expected:** User-friendly messages
4. **Expected:** Recovery works
5. **Expected:** No crashes

**Success Criteria:**
- ✅ Errors handled gracefully
- ✅ User-friendly messages
- ✅ Recovery works
- ✅ No crashes
- ✅ State preserved

---

### Step 11.3: Performance Optimization

**Goal:** Optimize performance for large directories

**Tasks:**
1. Profile application:
   - Identify bottlenecks
   - Optimize slow operations
   - Improve memory usage

2. Test with large dataset:
   - 10000+ files
   - Large files
   - Deep directory structure

**Testing Instructions:**
1. Test with large directory (10000+ files)
2. **Expected:** Indexing completes in reasonable time
3. **Expected:** TUI responsive
4. **Expected:** Memory usage reasonable
5. **Expected:** No freezing

**Success Criteria:**
- ✅ Handles large directories
- ✅ Responsive TUI
- ✅ Reasonable memory usage
- ✅ No performance issues

---

### Step 11.4: Final Testing and Documentation

**Goal:** Complete testing and documentation

**Tasks:**
1. Comprehensive testing:
   - All features
   - Edge cases
   - Error scenarios
   - Performance

2. Update documentation:
   - User guide
   - Developer guide
   - README
   - API documentation

**Testing Instructions:**
1. Test all features systematically
2. Test edge cases
3. Test error scenarios
4. **Expected:** All features work
5. **Expected:** Documentation complete

**Success Criteria:**
- ✅ All features tested
- ✅ Edge cases handled
- ✅ Documentation complete
- ✅ Ready for release

---

## Testing Checklist for Each Step

After completing each step, verify:

- [ ] Code runs without errors
- [ ] New functionality works as expected
- [ ] Previous functionality still works
- [ ] No regressions introduced
- [ ] Error handling works
- [ ] User experience is smooth
- [ ] Performance is acceptable

---

## Notes

- **Each step is independent:** You can test each step before moving to the next
- **Build incrementally:** Each step builds on previous steps
- **Test thoroughly:** Test each step manually before proceeding
- **Fix issues early:** Don't proceed if current step has issues
- **Document as you go:** Update documentation with each step

---

**Ready to start implementation? Begin with Step 1.1 and work through each step systematically!**

