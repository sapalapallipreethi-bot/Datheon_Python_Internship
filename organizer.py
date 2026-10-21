
import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

EXTENSION_MAP = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code"
}


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    moved = 0
    failed = 0

    print("\nAUTOMATED FILE ORGANIZER")
    print("-" * 40)

    try:
        entries = list(os.scandir(folder))
    except OSError as error:
        print(f"Cannot access folder: {error}")
        return

    for entry in entries:
        if not entry.is_file(follow_symlinks=False):
            continue

        source = Path(entry.path)
        category = EXTENSION_MAP.get(source.suffix.lower(), "Others")
        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder / source.name

            # Prevent overwriting files with duplicate names.
            counter = 1
            while destination.exists():
                destination = destination_folder / (
                    f"{source.stem}_{counter}{source.suffix}"
                )
                counter += 1

            shutil.move(str(source), str(destination))
            logging.info("Moved %s -> %s", source.name, category)
            moved += 1

        except (PermissionError, OSError) as error:
            logging.error("Could not move %s: %s", source.name, error)
            failed += 1

    print("\nEXECUTION SUMMARY")
    print("-" * 40)
    print(f"Files relocated: {moved}")
    print(f"Failed operations: {failed}")


if __name__ == "__main__":
    target = input("Enter folder path to organize: ").strip().strip('"')
    organize_files(target)
