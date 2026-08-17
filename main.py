import pyfiglet
from rich import print
from database import create_table, clear_index, search_code
from indexer import index_directory


title = pyfiglet.figlet_format("CodeVault", font = "standard")


def index_command():

    directory = input("Enter directory path: ").strip()

    try:

        count = index_directory(directory)

        print(f"\n[green]Indexed [blue]{count}[/blue] files successfully[/green]")

    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"\n[red]Error: [yellow]{error}[/yellow][/red]")

def search_command():

    keyword = input("Enter search keyword: ").strip()

    if not keyword:
        print("[red]search keyword cannot be empty[/red]")
        return

    results = search_code(keyword)

    if not results:
        print("\n[red]No result found[/red]")
        return

    print(f"\n[green]Found [blue]{len(results)}[/blue] result(s):[/green]\n")

    for path, content in results:

        print("=" *60)
        print(f"[yellow on magenta]File:[/yellow on magenta] [yellow]{path}[/yellow]")
        print("=" * 60)

        lines = content.splitlines()

        for line_number, line in enumerate(lines, start=1):

            if keyword.lower() in line.lower():
                print(f"[yellow on magenta]line no. {line_number}:[/yellow on magenta] {line}")

        print()


def main():

    create_table()

    while True:

        print(f"[bold cyan] {title} [/bold cyan]")
        print("1. Index directory")
        print("2. Search code")
        print("3. Clear indexing")
        print("4. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            index_command()

        elif choice == "2":
            search_command()

        elif choice == "3":
            clear_index()
            print("\n[green]Indexing cleared successfully[/green]")

        elif choice == "4":
            print("[yellow]Goodbye[/yellow]")
            break

        else:
            print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    main()