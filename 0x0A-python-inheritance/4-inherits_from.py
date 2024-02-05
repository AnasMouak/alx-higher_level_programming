#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherits from
    a specified class.

    Args:
    - obj (object): The object to be checked.
    - a_class (class): The class to check the object against.

    Returns:
    - bool: True if the object is an instance of a class that inherits from
    the specified class, False otherwise.
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
