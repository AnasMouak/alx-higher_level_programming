#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or a subclass.

    Args:
    - obj (object): The object to be checked.
    - a_class (class): The class to check the object against.

    Returns:
    - bool: True if the object is an instance of the specified class or a
    subclass, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
