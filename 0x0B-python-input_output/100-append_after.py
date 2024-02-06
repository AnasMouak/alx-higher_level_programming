#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new string after the first occurrence of a search string
    in a text file.

    Args:
    - filename (str): The name of the text file.
    - search_string (str): The string to search for in the text file.
    - new_string (str): The string to insert after the first occurrence
    of the search string.

    Returns:
    - None
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
