# CodeVault

CodeVault is an offline code indexing and searching tool built with Python.

It allows you to scan local projects, store their source code in a SQLite
database, and quickly search through the indexed code.

## Features

- Recursively scan project directories
- Support multiple programming languages
- Store source code locally using SQLite
- Search indexed code
- Display matching file paths
- Display matching line numbers
- Completely offline

## Project Structure

```text
CodeVault/
│
├── main.py
├── scanner.py
├── indexer.py
├── database.py
├── config.py
├── README.md
├── .gitignore
│
└── data/
    └── codevault.db