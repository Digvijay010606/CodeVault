import pathlib


# File extensions CodeVault can index
SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".php",
    ".html",
    ".css",
    ".sql",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".md",
    ".txt",
}


# Directories that should not be scanned
IGNORED_DIRECTORIES = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "node_modules",
    ".idea",
    ".vscode",
}


def scan_directory(target_directory):
    """
    Recursively scan a directory and return source files.
    """

    target_directory = pathlib.Path(target_directory)

    if not target_directory.exists():
        raise FileNotFoundError(
            f"Directory does not exist: {target_directory}"
        )

    if not target_directory.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {target_directory}"
        )

    files = []

    for item in target_directory.rglob("*"):

        # Skip ignored directories
        if any(part in IGNORED_DIRECTORIES for part in item.parts):
            continue

        if item.is_file() and item.suffix.lower() in SUPPORTED_EXTENSIONS:

            try:
                content = item.read_text(encoding="utf-8")

                files.append(
                    {
                        "path": str(item),
                        "content": content,
                    }
                )

            except (UnicodeDecodeError, PermissionError, OSError):
                # Skip files that cannot be read
                continue

    return files