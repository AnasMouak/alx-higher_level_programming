#!/usr/bin/python3
"""Defines a function to add an attribute to an object."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attr_name (str): The name of the attribute.
    - attr_value: The value of the attribute.

    Raises:
    - TypeError: If the object does not have a dictionary (__dict__) attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
