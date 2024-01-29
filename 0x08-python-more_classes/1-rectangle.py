#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """
    This class represents a Rectangle.

    Attributes:
    - __ width (int): The width of the Rectangle.
    - __ height (int): The height of the Rectangle.

    Methods:
    - __init__(self, width=0, height=0): Constructor method to initialize
    the Rectangle with a given width and height. Default width and height is 0.

    - width (property): Getter method for the width of the Rectangle.
    - width (setter): Setter method for updating the width of the Rectangle.
    - height (property): Getter method for the height of the Rectangle.
    - height (setter): Setter method for updating the height of the Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the specified width and height.

        Parameters:
        - width (int, optional): The width of the Rectangle. Default is 0.
        - height (int, optional): The height of the Rectangle. Default is 0.
        """
        self.width = width
        self.height = height

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
