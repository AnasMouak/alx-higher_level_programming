#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""


from models.base import Base

class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The identifier of the rectangle.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for the x-coordinate of the Rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for updating the x-coordinate of the Rectangle's
        position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y-coordinate of the Rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for updating the y-coordinate of the Rectangle's
        position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
        - int: The area of the Rectangle.
        """
        return self.__width * self.__height
    
    def display(self):
        """
        Displays the Rectangle with "#" symbols including its position (x, y).
        
        If the width or height is 0, it prints an empty line.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        result = ""
        for _ in range(self.__y):
            result += "\n"

        for _ in range(self.__height):
            result += " " * self.__x + "#" * self.__width + "\n"

        return result

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
        - str: A string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
    
    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle.

        Args:
            *args: Variable number of arguments in the order (width, height, x, y)
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:   
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.width = value
            elif key == 'height':
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
            dict: Dictionary containing the attributes of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
