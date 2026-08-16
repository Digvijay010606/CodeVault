from scanner import scan_directory
from database import insert_file


def index_directory(target_directory):
    """
    Scan a directory and store all source files in the database.
    """

    files = scan_directory(target_directory)

    indexed_count = 0

    for file in files:

        insert_file(
            file["path"],
            file["content"]
        )

        indexed_count += 1

    return indexed_count