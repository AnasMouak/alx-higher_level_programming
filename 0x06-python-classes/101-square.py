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
    - position (property): Getter method for the position of the square.
    - position (setter): Setter method for updating the position of the square.
    - area(self): Method to calculate the area of the square.
    - my_print(self): Method to print the square pattern using '#' character.
    - __str__(self): Method to return a string representation of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with the specified size.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
        - tuple: A tuple representing the position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        - value (tuple): A tuple representing the new position (x, y).

        Raises:
        - TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(j, int) and j >= 0 for j in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            return

        for _ in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        If the size is 0, returns an empty string.

        Returns:
        - str: The string representation of the square.
        """
        if self.__size == 0:
            return ""

        result = ""

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                result += "\n"

        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                result += "\n"

        return result
