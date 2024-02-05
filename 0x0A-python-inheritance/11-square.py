#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """
    Class representing a Square.

    Attributes:
    - __size (int): The size of the Square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the specified size.

        Parameters:
        - size (int): The size of the Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Computes the area of the Square.

        Returns:
        - int: The area of the Square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
        - str: A string representation of the Square.
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
