#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle where width == height.

    Attributes:
        All attributes are inherited from Rectangle:
        - id (int): The identifier of the square.
        - x (int): The x-coordinate of the square's position.
        - y (int): The y-coordinate of the square's position.
        - width (int): The width of the square.
        - height (int): The height of the square.

    Methods:
        All methods are inherited from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size of the Square.

        Returns:
        - int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size of the Square.

        Parameters:
        - value (int): The new width for the Rectangle.
        - value (int): The new height for the Rectangle.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square.

        Args:
            *args: Variable number of arguments in the order (id, size, x, y)
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: Dictionary containing the attributes of the Square.
        """
        #return self.__dict__
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string describing the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
