#!/usr/bin/python3
"""
Module provides a function for adding two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float, optional): The second number to be added.Defaults to 98.

    Returns:
    int: The sum of the two numbers, after converting them to integers
        if they are floats.

    Raises:
    TypeError: If either `a` or `b` is not an integer or a float.
    """

    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return int(a + b)
