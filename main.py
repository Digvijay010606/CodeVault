import pyfiglet

from rich.panel import Panel
from rich.table import Table

from config import console, clear_terminal, pause
from database import create_table, clear_index, search_code
from indexer import index_directory


# ==========================================
# CodeVault Graphical Title
# ==========================================

TITLE = pyfiglet.figlet_format(
    "CodeVault",
    font="standard"
)


# ==========================================
# UI Functions
# ==========================================

def show_title():
    """Display the CodeVault graphical title."""

    console.print(
        f"[bold cyan]{TITLE}[/bold cyan]"
    )

    console.print(
        "[dim]Offline Code Indexing & Search Tool[/dim]\n"
    )


def show_menu():
    """Display the main menu."""

    table = Table(
        title="Main Menu",
        show_header=False,
        border_style="cyan",
        padding=(0, 2),
    )

    table.add_row(
        "[bold cyan]1[/bold cyan]",
        "[white]Index Directory[/white]",
    )

    table.add_row(
        "[bold green]2[/bold green]",
        "[white]Search Code[/white]",
    )

    table.add_row(
        "[bold yellow]3[/bold yellow]",
        "[white]Clear Index[/white]",
    )

    table.add_row(
        "[bold red]4[/bold red]",
        "[white]Exit[/white]",
    )

    console.print(table)


# ==========================================
# Index Command
# ==========================================

def index_command():
    """Handle directory indexing."""

    clear_terminal()
    show_title()

    console.print(
        Panel(
            "[bold cyan]INDEX DIRECTORY[/bold cyan]\n\n"
            "Enter the path of the project you want to index.",
            border_style="cyan",
        )
    )

    directory = console.input(
        "\n[bold white]Directory path:[/bold white] "
    ).strip()

    if not directory:
        console.print(
            "\n[bold red]✗ Directory path cannot be empty.[/bold red]"
        )
        pause()
        return

    try:
        console.print(
            "\n[bold yellow]Scanning directory...[/bold yellow]"
        )

        count = index_directory(directory)

        console.print(
            Panel(
                f"[bold green]✓ Indexing completed successfully![/bold green]\n\n"
                f"Files indexed: [bold cyan]{count}[/bold cyan]",
                border_style="green",
            )
        )

    except (FileNotFoundError, NotADirectoryError) as error:

        console.print(
            Panel(
                f"[bold red]✗ Error[/bold red]\n\n"
                f"[yellow]{error}[/yellow]",
                border_style="red",
            )
        )

    pause()


# ==========================================
# Search Command
# ==========================================

def search_command():
    """Search indexed code."""

    clear_terminal()
    show_title()

    console.print(
        Panel(
            "[bold green]SEARCH CODE[/bold green]\n\n"
            "Search for a word or keyword inside indexed files.",
            border_style="green",
        )
    )

    keyword = console.input(
        "\n[bold white]Search keyword:[/bold white] "
    ).strip()

    if not keyword:

        console.print(
            "\n[bold red]✗ Search keyword cannot be empty.[/bold red]"
        )

        pause()
        return

    results = search_code(keyword)

    if not results:

        console.print(
            Panel(
                f"[bold red]No results found[/bold red]\n\n"
                f"No indexed code contains: "
                f"[yellow]{keyword}[/yellow]",
                border_style="red",
            )
        )

        pause()
        return

    console.print(
        f"\n[bold green]✓ Found "
        f"[cyan]{len(results)}[/cyan] matching file(s)[/bold green]\n"
    )

    for path, content in results:

        console.print(
            Panel(
                f"[bold yellow]File:[/bold yellow] "
                f"[white]{path}[/white]",
                border_style="cyan",
            )
        )

        lines = content.splitlines()

        found_line = False

        for line_number, line in enumerate(lines, start=1):

            if keyword.lower() in line.lower():

                found_line = True

                console.print(
                    f"  [bold magenta]Line "
                    f"{line_number:>4}[/bold magenta] "
                    f"[dim]│[/dim] {line}"
                )

        if not found_line:
            console.print(
                "[dim]Keyword found in file, but no matching "
                "line was displayed.[/dim]"
            )

        console.print()

    pause()


# ==========================================
# Clear Index Command
# ==========================================

def clear_index_command():
    """Clear all indexed data."""

    clear_terminal()
    show_title()

    console.print(
        Panel(
            "[bold yellow]CLEAR INDEX[/bold yellow]\n\n"
            "This will remove all currently indexed code "
            "from CodeVault.",
            border_style="yellow",
        )
    )

    confirmation = console.input(
        "\n[bold white]Are you sure? (y/n):[/bold white] "
    ).strip().lower()

    if confirmation == "y":

        clear_index()

        console.print(
            "\n[bold green]✓ Index cleared successfully.[/bold green]"
        )

    else:

        console.print(
            "\n[bold cyan]Operation cancelled.[/bold cyan]"
        )

    pause()


# ==========================================
# Main Application
# ==========================================

def main():

    create_table()

    while True:

        # ==================================
        # AUTO CLEAR TERMINAL
        # ==================================

        clear_terminal()

        show_title()
        show_menu()

        choice = console.input(
            "\n[bold white]Enter your choice:[/bold white] "
        ).strip()

        if choice == "1":

            index_command()

        elif choice == "2":

            search_command()

        elif choice == "3":

            clear_index_command()

        elif choice == "4":

            clear_terminal()

            show_title()

            console.print(
                Panel(
                    "[bold green]Thank you for using CodeVault![/bold green]\n\n"
                    "[dim]Goodbye 👋[/dim]",
                    border_style="cyan",
                )
            )

            break

        else:

            console.print(
                "\n[bold red]✗ Invalid choice.[/bold red] "
                "[yellow]Please select 1-4.[/yellow]"
            )

            pause()


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":
    main()