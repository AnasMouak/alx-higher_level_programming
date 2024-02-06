#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds command-line arguments to a JSON file.

    Reads command-line arguments and adds them to a JSON file named
    'add_item.json'.
    If the file already exists, it loads its contents and appends
    the new arguments.
    If the file does not exist, it creates a new file and saves the arguments.
    """
    file = "add_item.json"
    if os.path.exists(file):
        items = load_from_json_file(file)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, file)


if __name__ == "__main__":
    main()
