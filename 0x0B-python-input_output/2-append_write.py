#!/usr/bin/python3
"""Defines a function to append text to a file."""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Parameters:
    - filename (str): The name of the file to append to.
    - text (str): The text to be appended to the file.

    Returns:
    - int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
    return n
