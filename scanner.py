import pathlib

def scan_directory(target_directory):
    for item in target_directory.rglob("*.py"):
        if item.is_dir():
            return "Directory: {item}"
        elif item.is_file():
            return "File: {item}"
            try:
                content = item.read_text(encoding = 'utf-8')
                return content
            except Exception as e:
                print("Cannot read the content of file")

