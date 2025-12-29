# File Sorter

A privacy-focused, terminal-based file organization tool that uses LLM analysis to help you organize your files and directories efficiently. Built with Python and Textual for a modern TUI experience.

[![CodeQL](https://github.com/yourusername/file-sorter/workflows/CodeQL/badge.svg)](https://github.com/yourusername/file-sorter/security/code-scanning)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Key Features

- **Privacy-First**: All processing happens locally. No telemetry, no external data transmission without explicit permission
- **Efficient Large-Scale Processing**: Handles 10,000+ files efficiently with batch processing and checkpoint recovery
- **Version Control**: Complete history of all changes with easy rollback capability
- **Multi-Language Support**: English (default), Latvian, Russian
- **Smart Analysis**: Surface-level file analysis without reading full file contents
- **LLM Integration**: Optional AI-powered organization suggestions with multiple provider support (OpenAI, Anthropic, Ollama)

## Quick Start

### Installation

**Recommended (safest):**
```bash
pip install file-sorter
```

**Alternative (manual script review):**
```bash
# Download and review the script first
curl -fsSLO https://raw.githubusercontent.com/yourusername/file-sorter/main/install.sh
less install.sh  # Review the script
bash install.sh  # Run after review
```

**Development:**
```bash
git clone https://github.com/yourusername/file-sorter.git
cd file-sorter
pip install -e .
```

### Basic Usage

```bash
# Launch the tool
file-sorter

# Specify target directory
file-sorter --directory /path/to/directory

# Enable verbose logging
file-sorter --verbose
```

**Typical workflow:**
1. Launch tool and select target directory
2. Start indexing (scans files without reading full contents)
3. Request LLM analysis (optional) - get organization suggestions
4. Preview and execute changes - review before applying
5. Rollback if needed - restore previous versions anytime

## How It Works

File Sorter operates in three phases:

1. **Indexing**: Scans directory structure and extracts metadata (file types, sizes, dates). For text files, reads only first 512-1024 bytes as preview. Large files (>10MB) skip preview entirely.
2. **Analysis**: Optionally sends selected data to LLM for organization suggestions. You choose what to send: structure only, structure + metadata, or structure + metadata + previews.
3. **Organization**: Review suggested changes, execute selectively, and maintain version history for easy rollback.

<details>
<summary>Detailed implementation</summary>

### Indexing Phase

- Reads file headers (magic numbers) to determine file type
- Extracts metadata (EXIF for images, ID3 for audio, file size, modification date)
- For text files: reads only first 512-1024 bytes as preview
- Processes files in batches of 100 (configurable)
- Uses multiple threads for efficient processing
- Saves checkpoints after each batch to resume if interrupted

**What gets indexed:**
- File names and paths
- File types (determined by magic numbers, not extensions)
- File sizes and modification dates
- Metadata (EXIF, ID3 tags) - not file content
- Content preview (first 512-1024 bytes for text files only)

**What never gets indexed:**
- Full file contents
- Binary file data
- Large file contents (>10MB skip content preview entirely)

### Analysis Phase

1. **Data Selection**: Choose what to send to LLM (see LLM Payload Modes table below)
2. **Private File Filtering**: Files/directories marked as private are automatically excluded
3. **Warning Display**: Clear warning shows exactly what will be sent before any API call
4. **LLM Processing**: Sends selected data to chosen LLM provider
5. **Recommendation Generation**: LLM returns JSON with suggested operations

### Organization Phase

1. **Preview Display**: Shows all planned changes in a clear table
2. **Version Snapshot**: Before any changes, creates a directory structure snapshot (not file contents)
3. **Selective Execution**: Choose which changes to apply
4. **Safe Execution**: Performs file operations with validation
5. **Version Creation**: Saves new version with timestamp and description
6. **Rollback Available**: Any version can be restored at any time

</details>

## Privacy Model

### Local Processing

- **Indexing**: 100% local. Reads only file headers and metadata. Text file previews limited to first 512-1024 bytes.
- **Binary files**: Header only (magic numbers). No content reading.
- **Large files**: Files >10MB skip content preview entirely.
- **No telemetry**: Zero tracking, analytics, or usage statistics.
- **No external calls**: Except when you explicitly use LLM features.

### LLM Payload Modes

When using LLM analysis, you choose exactly what data is sent:

| Mode | What's Included | Use Case |
|------|----------------|----------|
| **Structure only** | File names, directory tree, file types | Recommended - minimal data exposure |
| **Structure + metadata** | Above + file sizes, dates, EXIF/ID3 tags | Better organization suggestions |
| **Structure + metadata + previews** | Above + first 512-1024 bytes of text files | Maximum context for LLM |

**Privacy protections:**
- Private files marked in index are never included in LLM requests
- Clear warning shows exactly what will be sent before any API call
- Local LLM (Ollama) option keeps everything on your computer
- No data is sent without explicit user permission

### Data Storage

**Stored locally in `.file_sorter/`:**
- Index files: metadata only (file names, types, sizes, modification dates)
- Content previews: first 512-1024 bytes for text files only
- File hash sums: SHA-256 for change detection
- Version snapshots: directory structure only (not file contents)

**Never stored:**
- Full file contents
- Binary file data
- User credentials or API keys (stored separately in config, never committed)

## Threat Model & Limitations

**Important considerations:**

1. **File names may be sensitive**: Even without reading contents, file names and paths are indexed and may reveal sensitive information
2. **Text previews may contain sensitive data**: First 512-1024 bytes of text files are read and may include sensitive information in headers/comments
3. **Cloud sync conflicts**: If files change during indexing (e.g., Dropbox/Drive sync), index may become inconsistent
4. **LLM recommendations may be incorrect**: Always review suggestions before executing. Use version snapshots for safety
5. **Version snapshots are structure-only**: File contents are not backed up - only directory structure and file metadata
6. **Index contains metadata**: File names, paths, sizes, and dates are stored locally - consider this if sharing `.file_sorter/` directory

## Security

### Security Scanning

This project uses GitHub's built-in security features:

- **[CodeQL](https://github.com/yourusername/file-sorter/security/code-scanning)** - Automated security scanning on every commit and pull request
- **[Dependabot](https://github.com/yourusername/file-sorter/security/dependabot)** - Automatic dependency vulnerability monitoring and updates

### How to Verify Security Claims

**Review the code:**
```bash
git clone https://github.com/yourusername/file-sorter.git
cd file-sorter
# Review source code in src/ directory
```

**Verify local-only processing:**
- Monitor network traffic: `netstat` or `tcpdump` during indexing (should show no external connections)
- Review code: Check `core/indexer.py` and `core/analyzer.py` for network calls
- Check config: Verify no telemetry endpoints configured

**Audit data storage:**
- Inspect `.file_sorter/` directory: Contains only metadata, no file contents
- Review index files: `cat .file_sorter/index.json` (verify no sensitive data)
- Check version files: Only directory structure, not file contents

## Configuration

Configuration is stored in `.file_sorter/config.json`:

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

<details>
<summary>All configuration options</summary>

- `language`: UI language (`en`, `lv`, `ru`)
- `llm_provider`: LLM provider (`openai`, `anthropic`, `ollama`)
- `llm_model`: Model name (e.g., `gpt-4`, `claude-3-opus`, `llama3`)
- `llm_api_key`: API key (stored securely, never committed)
- `batch_size`: Files per batch (default: 100)
- `thread_count`: Parallel processing threads (default: 4)
- `max_file_size_for_preview`: Skip preview for files larger than this (bytes, default: 10485760)
- `checkpoint_interval`: Save checkpoint every N batches (default: 1)

</details>

<details>
<summary>LLM Provider Setup</summary>

**OpenAI:**
1. Get API key from https://platform.openai.com/api-keys
2. Set in config: `"llm_provider": "openai"`, `"llm_model": "gpt-4"`
3. Add API key: `"llm_api_key": "sk-..."`

**Anthropic:**
1. Get API key from https://console.anthropic.com/
2. Set in config: `"llm_provider": "anthropic"`, `"llm_model": "claude-3-opus"`
3. Add API key: `"llm_api_key": "sk-ant-..."`

**Ollama (Local - Recommended):**
1. Install Ollama: https://ollama.ai/
2. Pull model: `ollama pull llama3`
3. Start server: `ollama serve`
4. Set in config: `"llm_provider": "ollama"`, `"llm_model": "llama3"`
5. No API key needed - everything stays local

</details>

## Uninstall & Cleanup

To completely remove File Sorter and all its data:

```bash
# Uninstall the package
pip uninstall file-sorter

# Remove all local data (indexes, versions, config)
rm -rf .file_sorter/

# Or remove from specific directory
rm -rf /path/to/directory/.file_sorter/
```

**What gets deleted:**
- Index files (`index.json`, `index_checkpoint.json`)
- Version snapshots (`versions/v*.json`)
- Configuration (`config.json`)
- All metadata and cached data

**Note**: This does not restore any file organization changes you've made. Use version rollback before uninstalling if you want to undo changes.

## Keyboard Shortcuts

- `F1` or `?` - Show help
- `Ctrl+C` - Cancel current operation
- `q` - Quit application
- Arrow keys - Navigate menus and tables
- `Enter` - Select/Confirm
- `Esc` - Go back/Cancel

## Frequently Asked Questions

<details>
<summary>Is my data safe?</summary>

Yes. All processing happens locally on your computer. No file contents are sent externally unless you explicitly choose to use LLM analysis, and even then, you control exactly what is sent. Private files marked as private are never included in any external communication.
</details>

<details>
<summary>Does this tool read my file contents?</summary>

No. The tool performs surface-level analysis only:
- Reads file headers (magic numbers) to determine file type
- Extracts metadata (EXIF, ID3 tags, file size, dates)
- For text files: reads only first 512-1024 bytes as preview
- Large files (>10MB) skip content preview entirely
- Never reads full file contents
</details>

<details>
<summary>What happens if the tool crashes during indexing?</summary>

The checkpoint system saves progress after each batch. If the tool crashes or is interrupted:
1. On next launch, it detects the checkpoint
2. Offers to resume from last checkpoint
3. Only processes remaining files
4. No work is lost
</details>

<details>
<summary>Can I undo changes?</summary>

Yes. Every change creates a version snapshot (directory structure only, not file contents). You can:
- Rollback to any previous version
- Restore individual files
- Restore entire directory structure
- View version history
</details>

<details>
<summary>How do I know what will be sent to LLM?</summary>

Before any LLM API call:
1. Clear warning dialog shows exactly what will be sent
2. You can review the data payload
3. Private files are automatically excluded
4. You must explicitly confirm before sending
5. Option to cancel at any time
</details>

<details>
<summary>Can I use this without internet?</summary>

Yes, if using local LLM (Ollama):
- Install Ollama locally
- Pull desired model
- Configure tool to use Ollama
- Everything works offline
- No internet connection needed
</details>

<details>
<summary>How long does indexing take?</summary>

Depends on:
- Number of files (100 files: ~10 seconds, 10,000 files: ~10-30 minutes)
- File sizes (large files skip preview, faster)
- System performance (CPU, disk speed)
- Configuration (batch size, thread count)

Use checkpoint system to pause/resume as needed.
</details>

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/yourusername/file-sorter.git
cd file-sorter
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Style

We use `black` for code formatting and `ruff` for linting:

```bash
black src/
ruff check src/
```

## Security Reporting

If you discover a security vulnerability, please report it to [security@example.com](mailto:security@example.com). Do not open a public issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [Full Documentation](https://file-sorter.readthedocs.io/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/file-sorter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/file-sorter/discussions)
- **Security**: [Security Policy](SECURITY.md)

## Acknowledgments

- Built with [Textual](https://textual.textualize.io/) for the TUI framework
- Uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Inspired by the need for privacy-focused file organization tools

---

**Important**: This tool processes your files locally. Always review changes before executing them. Use version control features to maintain the ability to rollback. For security concerns, see [SECURITY.md](SECURITY.md).
