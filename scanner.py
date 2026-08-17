from pathlib import Path
from rich import print

SUPPORTED_EXTENSIONS = {
    ".py",
    ".c",
    ".cpp",
    ".js",
    ".java",
    ".html",
    ".css",
    ".h",
    ".hpp"
}

def scan_directory(target_directory):

    target_directory = Path(target_directory)

    if not target_directory.exists():
        raise FileNotFoundError(
            print(f"[red]Directory does not exists:[/red] [yellow]{target_directory}[/yellow]")
        )

    if not target_directory.is_dir():
        raise NotADirectoryError(
            print(f"[red]Not a Directory:[/red] [yellow]{target_directory}[/yellow]")
        )

    files = []

    for file in target_directory.rglob("*"):

        if not file.is_file():
            continue
        
        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        if any(part in {"__pycache__", ".git", "venv", ".venv"} for part in file.parts):
            continue

        try:
            content = file.read_text(
                encoding = 'utf-8',
                errors = 'ignore'
            )

            files.append({
                "path" : file,
                "content" : content
            })

        except OSError as error:
            print(f"[red]Could not read[/red] [yellow]{file}:[/yellow] [red]{error}[/red]")

    return files
