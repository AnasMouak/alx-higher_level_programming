#!/usr/bin/python3
"""
Module provides a function for printing a square of a specified size.

"""


def print_square(size):
    """
    Prints a square made of '#' characters with the specified size.

    Parameters:
    - size (int): The size of the square. Must be a non-negative integer.

    Returns:
    None

    Raises:
    TypeError: If `size` is not an integer or is a negative float.
    ValueError: If `size` is a negative integer.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
