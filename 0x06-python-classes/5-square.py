#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    This class represents a square.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Constructor method to initialize
    the square with a given size. Default size is 0.

    - size (property): Getter method for the size of the square.
    - size (setter): Setter method for updating the size of the square.
    - area(self): Method to calculate the area of the square.
    - my_print(self): Method to print the square pattern using '#' character.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with the specified size.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size of the square.

        Parameters:
        - value (int): The new size for the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square pattern using '#' character.

        If the size is 0, it prints an empty line.

        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
