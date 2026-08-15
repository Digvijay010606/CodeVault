import pathlib
from scanner import scan_directory


def indexer():
    content = scan_directory(pathlib.Path(input("Enter the directory path: ")))
    return content

print(indexer())


    