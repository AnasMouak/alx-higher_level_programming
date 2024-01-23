#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a square.

    Attributes:
    - size (int): The size of the square.

    Methods:
    - __init__(self, size): Constructor method to initialize
    the square with a given size.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the specified size.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
