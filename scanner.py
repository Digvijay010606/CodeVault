import pathlib

def scan_directory(target_directory):
    for item in target_directory.rglob("*.py"):
        if item.is_dir():
            print(f"Directory: {item}")
        elif item.is_file():
            print(f"File: {item}")
            print("--------------- Reading content----------------------")
            try:
                content = item.read_text(encoding = 'utf-8')
                print(content)
            except Exception as e:
                print("Cannot read the content of file")


