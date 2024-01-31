#!/usr/bin/python3
"""
Module provides a function for printing a person's name.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name by combining the first name and last name.

    Parameters:
    - first_name (str): The first name of the person.
    - last_name (str, optional): The last name of the person.
                                Defaults to an empty string.

    Returns:
    None

    Raises:
    TypeError: If either `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
