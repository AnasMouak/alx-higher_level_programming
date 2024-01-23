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
    def __init__(self, size=0):
        """
        Initializes a Square instance with the specified size.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
