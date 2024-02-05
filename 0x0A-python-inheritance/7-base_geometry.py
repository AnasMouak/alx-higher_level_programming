#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """
    Empty class representing the base geometry.

    Methods:
    - area(self): Raises an exception with the message
    "area() is not implemented."
    - integer_validator(self, name, value): Validates if a value is
    a positive integer.
    """
    def area(self):
        """
        Raises an exception with the message "area() is not implemented."

        Returns:
        - None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
        - name (str): The name of the value.
        - value (int): The value to be validated.

        Returns:
        - None

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
