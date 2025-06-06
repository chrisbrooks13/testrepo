# show_structure.py
# Prints a simple directory tree up to depth 3.
# Used when the `tree` command is unavailable.

import os

MAX_DEPTH = 3


def walk(dir_path: str, prefix: str = "", depth: int = 0) -> None:
    """Recursively print entries up to MAX_DEPTH."""
    if depth > MAX_DEPTH:
        return
    try:
        entries = sorted(os.listdir(dir_path))
    except FileNotFoundError:
        return

    for idx, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        connector = "└── " if idx == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "    " if idx == len(entries) - 1 else "│   "
            walk(path, prefix + extension, depth + 1)


def main() -> None:
    root = os.path.dirname(os.path.abspath(__file__))
    print(os.path.basename(root))
    walk(root)


if __name__ == "__main__":
    main()
