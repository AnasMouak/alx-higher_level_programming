#!/usr/bin/python3
"""
Module provides a function for formatting text
by adding line breaks after specific characters.

"""


def text_indentation(text):
    """
    Formats the input text by adding line breaks
    after specific characters (., ?, :).

    Parameters:
    - text (str): The text to be formatted.

    Returns:
    None

    Raises:
    TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    lineI = ""
    for i in text:
        lineI += i
        if i in characters:
            print(lineI.strip())
            print()
            lineI = ""

    print(lineI.strip(), end="")
