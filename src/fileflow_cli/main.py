"""Main entry point for FileFlowCLI."""

import sys
from pathlib import Path

# Add src directory to path for direct execution
if __name__ == "__main__":
    src_path = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(src_path))

from fileflow_cli.tui.app import FileFlowCLIApp


def main():
    """Main entry point for the FileFlowCLI application."""
    app = FileFlowCLIApp()
    app.run()


if __name__ == "__main__":
    main()

