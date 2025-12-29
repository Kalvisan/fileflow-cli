# Simplified Development Plan - MVP with Advanced Core Features

## Core Features

### What We're Building:
1. ✅ Basic file indexing (recursive, saves to JSON)
2. ✅ TUI with main screen and indexing screen (top-like layout)
3. ✅ LLM analysis (OpenAI ChatGPT-5.2 - primary, others in next phase)
4. ✅ File operations (move, rename) with advanced conflict resolution
5. ✅ Version control (save structure, rollback)
6. ✅ Translation system (English default, all text in translation files for easy i18n)
7. ✅ Advanced checkpoint system (pause/resume, handles large file counts)
8. ✅ Dynamic error handling (user-friendly + developer details)
9. ✅ **Parallel processing system** (dynamic, reusable, TUI-friendly) - from the start
10. ✅ Advanced search (multi-language support) - later step
11. ✅ Multi-select operations - later step

### What We're Skipping for MVP:
- ❌ Multiple LLM providers → Only OpenAI ChatGPT-5.2 (others in next phase)
- ❌ Custom LLM endpoint → Next phase
- ❌ Complex exceptions → Skip for now
- ❌ Virtualization → Basic table (optimize later if needed)
- ❌ Incremental indexing → Full re-index each time (can optimize later)

---

## Step-by-Step Implementation (14 Steps)

### Step 1: Project Setup
- Create project structure:
  ```
  file_sorter/
  ├── src/
  │   └── file_sorter/
  │       ├── __init__.py
  │       └── main.py
  ├── requirements.txt
  ├── .gitignore
  ├── README.md
  └── setup.py
  ```
- Setup.py with entry point: `file-sorter`
- Requirements.txt: `textual>=0.50.0`, `rich>=13.0.0`, `openai>=1.0.0`
- Basic main.py that prints "File Sorter TUI - Starting..."

**Test:** `pip install -e . && file-sorter` → Should print "File Sorter TUI - Starting..."

---

### Step 2: Translation System Foundation
- Create `src/file_sorter/i18n/` directory:
  ```
  i18n/
  ├── __init__.py
  ├── translations.py
  └── en.json
  ```
- Create `en.json` with all UI strings:
  ```json
  {
    "app": {
      "title": "File Sorter",
      "welcome": "Welcome to File Sorter"
    },
    "main_menu": {
      "title": "Main Menu",
      "start_indexing": "Start Indexing",
      "analyze_llm": "Analyze with LLM",
      "settings": "Settings",
      "exit": "Exit"
    },
    "errors": {
      "file_not_found": "File not found: {path}",
      "permission_denied": "Permission denied: {path}"
    }
  }
  ```
- Create `translations.py`:
  - Function `t(key, **kwargs)` to get translation
  - Load language from config (default: "en")
  - All UI text uses translations (even if only English for now)

**Why:** Makes it easy to add other languages later - just add `lv.json`, `ru.json` and update dropdown

**Test:** Run program → All text loads from `en.json`, can change language in config

---

### Step 3: Configuration System
- Create `src/file_sorter/utils/config.py`:
  - Function to find/create `.file_sorter/` directory in working directory
  - Function to load/create `config.json` with defaults:
    ```json
    {
      "language": "en",
      "llm_provider": "openai",
      "llm_model": "gpt-5.2",
      "llm_api_key": "",
      "batch_size": 100,
      "thread_count": 4
    }
    ```
  - Check parent directories for existing `.file_sorter/` (offer to use parent's)

**Test:** Run program → Should create `.file_sorter/config.json` in current directory

---

### Step 4: Dynamic Error Handling System
- Create `src/file_sorter/utils/error_handler.py`:
  - Centralized error handling class
  - Error types: FileOperationError, LLMError, IndexingError, ConfigError
  - Function `handle_error(error, context)`:
    - Logs detailed error for developer (file, line, stack trace, context)
    - Returns user-friendly message
    - Stores error details for debugging
  - Error display:
    - User sees: Simple, clear message (e.g., "File not found: document.txt")
    - Developer sees: Full details (file path, line number, stack trace, context)
    - Option to show/hide details (toggle in UI)
  - Error recovery:
    - Suggests fixes when possible
    - Can retry operations
    - Rollback on critical errors

**Why:** Proper error handling from start makes debugging easier and user experience better

**Test:**
- Trigger file error → Should show user-friendly message
- Toggle details → Should show developer details
- Test LLM error → Should handle gracefully

---

### Step 5: Basic TUI
- Create `src/file_sorter/tui/app.py`:
  - Basic Textual App class
  - Load translations
  - Main screen with header (top section) and content area (bottom section)
  - Top-like layout: Header ~20% height, Content ~80% height
  - Exit on 'q'

**Test:** Run program → TUI opens with top-like layout, can exit with 'q'

---

### Step 6: Advanced Checkpoint System
- Create `src/file_sorter/storage/checkpoint_manager.py`:
  - Function `save_checkpoint(progress_data, path)`:
    - Saves to `.file_sorter/index_checkpoint.json`
    - Includes: processed files list, batch number, total files, file hashes
    - Saves quickly (doesn't block indexing)
  - Function `load_checkpoint(path)`:
    - Loads checkpoint
    - Validates checkpoint integrity
    - Returns checkpoint data or None
  - Function `clear_checkpoint(path)`:
    - Deletes checkpoint when complete
  - Checkpoint structure:
    ```json
    {
      "checkpoint_version": "1.0",
      "started_at": "2024-01-01T12:00:00",
      "last_updated": "2024-01-01T12:30:00",
      "total_files": 10000,
      "processed_files": 7500,
      "processed_paths": ["file1.txt", "file2.jpg", ...],
      "file_hashes": {"file1.txt": "abc123...", ...},
      "current_batch": 75,
      "total_batches": 100,
      "status": "in_progress"
    }
    ```

**Why:** Essential for handling large file counts and allowing pause/resume

**Test:**
- Start indexing → Checkpoint saved after each batch
- Interrupt indexing → Checkpoint exists
- Resume → Should continue from checkpoint

---

### Step 7: File Indexing with Checkpoint and Parallel Processing Integration
- Create `src/file_sorter/core/parallel_executor.py`:
  - Dynamic parallel processing system (reusable across codebase)
  - Class `ParallelExecutor`:
    - Configurable thread pool (from config: `thread_count`, default 4)
    - Thread-safe progress tracking
    - Function `execute_parallel(tasks, callback=None)`:
      - Executes tasks in parallel
      - Thread-safe progress updates
      - Returns results in order
      - Handles errors gracefully
    - Function `execute_batch_parallel(batches, callback=None)`:
      - Processes batches in parallel
      - Thread-safe batch tracking
      - Yields progress updates
  - Easy to use: `executor.execute_parallel(file_tasks, progress_callback)`
  - TUI-friendly: Progress callbacks work seamlessly with TUI updates

- Create `src/file_sorter/core/indexer.py`:
  - Function `index_directory(path, checkpoint=None)`:
    - Recursively walks directory
    - Uses `ParallelExecutor` for parallel file processing
    - Processes files in batches (configurable, default 100)
    - After each batch:
      - Saves checkpoint
      - Yields progress update (thread-safe)
    - Collects: path, name, size, modified date, file hash
    - Can pause/resume at any time
    - Handles large file counts efficiently (10,000+ files)
    - Parallel processing: Multiple files processed simultaneously
  - Function `resume_indexing(checkpoint_path)`:
    - Loads checkpoint
    - Skips already processed files
    - Continues from last batch with parallel processing
  - Create `src/file_sorter/storage/index_storage.py`:
    - Save/load index.json
    - Include `indexed_at` timestamp

**Why:** Parallel processing from start ensures system can handle large file counts efficiently and provides reusable infrastructure for future features

**Test:**
- Start indexing → Multiple files processed simultaneously
- Check CPU usage → Should use multiple cores
- Progress updates → Should be thread-safe and accurate
- Start indexing → Progress updates, checkpoint saved
- Interrupt (Ctrl+C) → Checkpoint saved
- Resume → Continues from checkpoint with parallel processing
- Complete → Index saved, checkpoint deleted

---

### Step 8: Indexing Status Check and TUI Integration
- Update main screen:
  - On startup, check if `index.json` exists
  - Check `indexed_at` timestamp
  - If checkpoint exists → Offer to resume
  - If no index → Show "Indexing: Not Started", block functions
  - If indexed → Show "Indexing: Complete (Last: {timestamp})", enable functions
- Create indexing screen (`tui/screens/indexing.py`):
  - Top section: Progress bar, files processed/total, speed, ETA
  - Bottom section: Live file processing table
  - Updates in real-time (every 100-500ms)
  - Can pause ('p'), resume ('r'), cancel ('c')

**Test:**
- Fresh start → Functions blocked
- Start indexing → Indexing screen shows progress
- Pause → Can resume
- Complete → Returns to main screen, functions enabled

---

### Step 9: File Table Display
- Create `src/file_sorter/tui/widgets/file_table.py`:
  - DataTable widget
  - Loads from `index.json`
  - Columns: Name, Path, Type, Size, Modified
  - Basic scrolling
  - Shows "No files indexed" if empty

**Test:** After indexing → Table shows all files, can scroll

---

### Step 10: LLM Integration (OpenAI ChatGPT-5.2)
- Create `src/file_sorter/core/llm_client.py`:
  - OpenAI client class
  - Function `send_request(prompt, data, api_key)`:
    - Formats request with file structure
    - Sends to OpenAI API (ChatGPT-5.2)
    - Handles errors with error_handler
    - Returns response
  - Function `prepare_request(index_data, user_instructions)`:
    - Formats data as JSON
    - Adds user instructions
    - Returns JSON payload
  - Error handling:
    - API errors → Handled by error_handler
    - Network errors → Retry with backoff
    - Invalid responses → Request retry
- Create LLM analysis screen:
  - Shows JSON preview before sending
  - User enters instructions: "How should I organize these files?"
  - User confirms before sending
  - Shows progress indicator
  - Displays response

**Test:**
- Enter API key in config
- Click "Analyze with LLM"
- Enter instructions
- Preview JSON → Should show what will be sent
- Send → Should get response from ChatGPT-5.2
- Test error handling → Should handle API errors gracefully

---

### Step 11: Advanced Conflict Resolution System
- Create `src/file_sorter/core/conflict_resolver.py`:
  - Centralized conflict resolution logic (reusable)
  - Conflict types:
    - File exists at destination
    - Symlink encountered
    - Hard link encountered
    - Permission denied
  - Function `resolve_conflict(conflict_type, source, destination, context)`:
    - Detects conflict type
    - Shows options to user:
      - File exists: overwrite, skip, rename (with auto-numbering)
      - Symlink: follow, ignore, treat as file
      - Hard link: treat as separate, maintain link, skip
    - Returns user choice
    - Saves preference for similar conflicts
  - Function `apply_resolution(choice, source, destination)`:
    - Executes chosen resolution
    - Handles edge cases
  - Conflict resolution dialog:
    - Shows conflict details
    - Clear options
    - Can set default for similar conflicts
    - Preview what will happen

**Why:** Advanced conflict resolution is essential and reusable across the system

**Test:**
- Try to move file to existing destination → Should detect conflict
- Choose resolution → Should apply correctly
- Test symlink → Should handle correctly
- Test hard link → Should handle correctly
- Set preference → Should remember for similar conflicts

---

### Step 12: Version System
- Create `src/file_sorter/core/version_manager.py`:
  - Function `create_version(description)`:
    - Saves directory structure to `versions/vN.json`
    - Includes timestamp, description
    - Only saves structure (paths, names), not file contents
  - Function `list_versions()`:
    - Returns list of all versions with metadata
  - Function `get_version(version_num)`:
    - Loads version data
  - Function `rollback_to_version(version_num)`:
    - Loads version structure
    - Compares with current
    - Creates rollback plan
    - Uses conflict_resolver for conflicts
    - Returns operations needed
- Create version list screen:
  - Shows all versions
  - Can select version to rollback
  - Preview rollback changes

**Test:**
- Create version → Should save to `versions/v1.json`
- Make changes
- Create version → Should save v2
- Rollback to v1 → Should restore structure
- Test conflicts during rollback → Should use conflict_resolver

---

### Step 13: File Operations with Conflict Resolution
- Create `src/file_sorter/core/file_operations.py`:
  - Function `move_file(source, destination, conflict_resolver)`:
    - Validates paths
    - Checks for conflicts
    - Uses conflict_resolver if conflict detected
    - Moves file
    - Returns success/error
  - Function `rename_file(source, new_name, conflict_resolver)`:
    - Similar to move_file
  - Function `create_directory(path)`:
    - Creates directory
    - Handles errors
  - Function `execute_operations(operations, conflict_resolver)`:
    - Groups operations into transaction
    - Validates all before execution
    - Executes all operations
    - Uses conflict_resolver for each conflict
    - If any fails → rollback all
    - Creates version before transaction
- Create operation preview screen:
  - Shows planned operations
  - User confirms
  - Executes operations
  - Shows conflicts as they occur
  - Uses conflict_resolver for each conflict

**Test:**
- Get LLM recommendations
- Preview operations → Should show all operations
- Execute → Should handle conflicts using conflict_resolver
- Test transaction rollback → Should rollback all on failure

---

### Step 14: Advanced Search (Multi-language)
- Update `file_table.py`:
  - Add search input field
  - Function `search_files(query, language="en")`:
    - Search by: name, type, path, content preview
    - Multi-language support:
      - Handles English, Latvian, Russian characters
      - Fuzzy matching
      - Case-insensitive
    - Real-time filtering as user types
  - Search highlighting:
    - Highlights matching text in results
  - Keyboard shortcut: '/' to focus search

**Why:** Advanced search is important but can be added later in the workflow

**Test:**
- Press '/' → Search focused
- Type "txt" → Should filter .txt files
- Type "документ" (Russian) → Should find Russian file names
- Type "faili" (Latvian) → Should find Latvian file names
- Fuzzy search → "txt" should find "text", "document.txt"

---

### Step 15: Multi-select Operations (Optional - Later)
- Update `file_table.py`:
  - Space key toggles selection
  - Ctrl+A selects all visible
  - Ctrl+D deselects all
  - Visual indicator for selected files
  - Show selected count
- Update file operations:
  - Can operate on multiple selected files
  - Batch operations use conflict_resolver for each file

**Why:** Useful feature but can be added after core functionality works

**Test:**
- Select multiple files → Should highlight
- Operate on selected → Should process all selected files
- Conflicts → Should resolve each conflict

---

## Error Handling Details

### Error Types:
1. **FileOperationError**: File not found, permission denied, disk full
2. **LLMError**: API error, network error, invalid response
3. **IndexingError**: File access error, checkpoint corruption
4. **ConfigError**: Invalid config, missing API key

### Error Display:
- **User sees**: "File not found: document.txt. Please check the file path."
- **Developer sees**: 
  ```
  FileOperationError: File not found
  Path: /path/to/document.txt
  File: file_operations.py, Line: 45
  Stack trace: ...
  Context: {'operation': 'move', 'source': '...', 'destination': '...'}
  ```

### Error Recovery:
- Suggests fixes: "Did you mean: /path/to/document.txt?"
- Can retry operation
- Rollback on critical errors
- Logs all errors for debugging

---

## Translation System Details

### Structure:
- All UI text in `en.json`
- Easy to add `lv.json`, `ru.json` later
- Language dropdown in settings (for future)
- All error messages translatable

### Example:
```json
{
  "main_menu": {
    "start_indexing": "Start Indexing",
    "analyze_llm": "Analyze with LLM"
  },
  "errors": {
    "file_not_found": "File not found: {path}"
  }
}
```

Usage: `t("main_menu.start_indexing")` → "Start Indexing"

---

## Conflict Resolution Details

### Reusable Logic:
- `conflict_resolver.py` handles all conflicts
- Used by: file operations, rollback, any operation that might conflict
- Consistent behavior across system

### Conflict Types:
1. **File exists**: overwrite, skip, rename (auto-number: file_1.txt)
2. **Symlink**: follow symlink, ignore symlink, treat as regular file
3. **Hard link**: treat as separate file, maintain link, skip
4. **Permission**: skip file, show warning

### User Experience:
- Clear dialog showing conflict
- Preview what will happen
- Can set default for similar conflicts
- Batch conflicts handled one by one

---

## Testing Checklist

After each step:
- [ ] Code runs without errors
- [ ] New feature works
- [ ] Previous features still work
- [ ] Error handling works correctly
- [ ] Can test manually
- [ ] Error messages are user-friendly
- [ ] Developer details available

---

## Summary

**Total Steps: 15** (core: 14, optional: 1)

**Core Features:**
- ✅ Translation system foundation (English, ready for i18n)
- ✅ Advanced checkpoint system (pause/resume, large files)
- ✅ Dynamic error handling (user + developer views)
- ✅ **Parallel processing system** (dynamic, reusable, TUI-friendly) - from the start
- ✅ Advanced conflict resolution (reusable, comprehensive)
- ✅ LLM integration (OpenAI ChatGPT-5.2)
- ✅ Version control with rollback
- ✅ File operations with conflict handling

**Later Features:**
- Advanced search (Step 14)
- Multi-select (Step 15)

**Estimated Time:** 3-5 days for experienced developer, 1-2 weeks for learning

---

**Ready to start? Begin with Step 1 and work through systematically!**
