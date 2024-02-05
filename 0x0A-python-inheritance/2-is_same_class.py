#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
    - obj (object): The object to be checked.
    - a_class (class): The class to check the object against.

    Returns:
    - bool: True if the object is an instance of the specified class,
    False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
