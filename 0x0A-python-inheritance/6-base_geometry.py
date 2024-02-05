#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """
    Empty class representing the base geometry.

    Methods:
    - area(self): Raises an exception with the message "area() is not
    implemented."
    """
    def area(self):
        """
        Raises an exception with the message "area() is not implemented."

        Returns:
        - None
        """
        raise Exception("area() is not implemented")
