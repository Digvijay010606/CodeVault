import pathlib
from scanner import scan_directory

print("hello welcome to CodeVault")

scan_directory(pathlib.Path(input("Enter the directory path: ")))
