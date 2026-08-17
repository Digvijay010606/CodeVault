from database import insert_file, clear_index
from scanner import scan_directory


def index_directory(target_directory):
    """
    Scan a directory and create a fresh index.
    """

    # Remove previous indexed data
    clear_index()

    # Scan the directory
    files = scan_directory(target_directory)

    indexed_count = 0

    for file in files:
        insert_file(
            file["path"],
            file["content"],
        )

        indexed_count += 1

    return indexed_count