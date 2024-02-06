#!/usr/bin/python3
"""Defines a function to Loads a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Parameters:
    - filename (str): The name of the file to load the object from.

    Returns:
    - obj: The Python object loaded from the JSON file.
    """
    with open(filename,  encoding="utf-8") as f:
        return json.loads(f.read())
