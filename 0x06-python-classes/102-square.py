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
    - __eq__(self, other): Method for equality comparison.
    - __ne__(self, other): Method for inequality comparison.
    - __gt__(self, other): Method for greater than comparison.
    - __ge__(self, other): Method for greater than or equal to comparison.
    - __lt__(self, other): Method for less than comparison.
    - __le__(self, other): Method for less than or equal to comparison.
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

    def __eq__(self, other):
        """Equality comparison based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison based on square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison based on square area."""
        return self.area() <= other.area()
