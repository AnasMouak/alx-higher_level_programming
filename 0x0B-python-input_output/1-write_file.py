#!/usr/bin/python3
"""Defines a function to write text to a file."""


def write_file(filename="", text=""):
    """
    Writes text to a file.

    Parameters:
    - filename (str): The name of the file to write to.
    - text (str): The text to be written to the file.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return n
