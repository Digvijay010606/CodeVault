from database import create_table, clear_index, search_code
from indexer import index_directory


def index_command():

    directory = input("Enter directory path: ").strip()

    try:

        count = index_directory(directory)

        print(f"\nIndexed {count} files successfully")

    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"\nError: {error}")

def search_command():

    keyword = input("Enter search keyword: ").strip()

    if not keyword:
        print("search keyword cannot be empty")
        return

    results = search_code(keyword)

    if not results:
        print("\nNo result found")
        return

    print(f"\nFound {len(results)} result(s):\n")

    for path, content in results:

        print("=" *60)
        print(f"File: {path}")
        print("=" * 60)

        lines = content.splitlines()

        for line_number, line in enumerate(lines, start=1):

            if keyword.lower() in line.lower():
                print(f"line no. {line_number}: {line}")

        print()


def main():

    create_table()

    while True:

        print("\n========== CodeVault ==========\n")
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
            print("\nIndexing cleared successfully")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()