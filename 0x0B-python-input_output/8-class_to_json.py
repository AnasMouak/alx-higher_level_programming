#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Converts a class instance to a dictionary representation.

    Args:
        obj: A class instance.

    Returns:
        dict: A dictionary containing the attributes of the class instance.
    """
    return obj.__dict__
