#!/usr/bin/python3
"""Defines a function to Converts a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Parameters:
    - my_obj: The Python object to be converted.

    Returns:
    - str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
