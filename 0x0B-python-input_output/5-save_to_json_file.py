#!/usr/bin/python3
"""Defines a function to Saves a Python object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Parameters:
    - my_obj: The Python object to be saved.
    - filename (str): The name of the file to save the object to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        n = json.dumps(my_obj)
        f.write(n)
