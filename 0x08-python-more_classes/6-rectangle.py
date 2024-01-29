#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """
    This class represents a Rectangle.

    Attributes:
    - width (int): The width of the Rectangle.
    - height (int): The height of the Rectangle.
    - number_of_instances (int): Tracks the number of Rectangle
    instances created.

    Methods:
    - __init__(self, width=0, height=0): Constructor method to initialize
    the Rectangle with a given width and height. Default width and height is 0.

    - width (property): Getter method for the width of the Rectangle.
    - width (setter): Setter method for updating the width of the Rectangle.
    - height (property): Getter method for the height of the Rectangle.
    - height (setter): Setter method for updating the height of the Rectangle.
    - area (self): Method to calculate the area of the Rectangle.
    - perimeter (self): Method to calculate the perimeter of the Rectangle.
    - print(self): Method to print the Rectangle pattern using '#' character.
    - __str__(self): Method to return a string representation of the Rectangle.
    - __repr__(self):Method to return a string representation of the Rectangle.
    - __del__(self): Method that Prints a message when an instance of Rectangle
    is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the specified width and height.

        Parameters:
        - width (int, optional): The width of the Rectangle. Default is 0.
        - height (int, optional): The height of the Rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width of the Rectangle.

        Returns:
        - int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for updating the width of the Rectangle.

        Parameters:
        - value (int): The new width for the Rectangle.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the Rectangle.

        Returns:
        - int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for updating the height of the Rectangle.

        Parameters:
        - value (int): The new height for the Rectangle.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
        - int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the Rectangle.

        Returns:
        - int: The perimeter of the Rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def print(self):
        """
        Prints the Rectangle pattern using '#' character.

        If the width or height is 0, it prints an empty line.

        """
        if self.__width == 0 or self.__height == 0:
            print()

        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        If the height or width is 0, returns an empty string.

        Returns:
        - str: The string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""

        for i in range(self.__height):

            result += "#" * self.__width
            if i < self.__height - 1:
                result += "\n"

        return result

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a farewell message when an instance of Rectangle is deleted
        and decrements the number_of_instances count.

        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
