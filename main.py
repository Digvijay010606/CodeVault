import pathlib

print("hello welcome to CodeVault")

target_directory = pathlib.Path(input("Enter the directory: "))

for item in target_directory.rglob("*.py"):
    if item.is_file():
        print(f"file: {item}")
        print("----------------- Reading content:")
        try:
            content = item.read_text(encoding = 'utf-8')
            print(content)
        except Exception as e:
            print("Could not read content")

    elif item.is_dir():
        print(f"directory: {item}")

