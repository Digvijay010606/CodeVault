import os
import pathlib

from rich.console import Console


# ==============================
# Paths
# ==============================

BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "codevault.db"


# ==============================
# Rich Console
# ==============================

console = Console()


# ==============================
# Terminal Utilities
# ==============================

def clear_terminal():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Wait for the user before continuing."""
    console.input("\n[dim]Press Enter to continue...[/dim]")


def create_data_directory():
    """Create the data directory if it does not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)