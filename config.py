import pathlib

def database_path():
    base_dir = pathlib.Path("/database")
    file_path = base_dir / "database.db"
    return file_path

