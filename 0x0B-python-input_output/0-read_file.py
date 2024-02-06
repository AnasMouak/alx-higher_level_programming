#!/usr/bin/python3
"""Defines a function to read and print the contents of a file."""


def read_file(filename=""):
    """
    Reads the contents of a file and prints them.

    Parameters:
    - filename (str): The name of the file to be read.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
