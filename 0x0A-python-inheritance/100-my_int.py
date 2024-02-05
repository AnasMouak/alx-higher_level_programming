#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    Class representing a custom integer.

    Methods:
    - __eq__(self, value): Checks if two integers are not equal.
    - __ne__(self, value): Checks if two integers are equal.
    """
    def __eq__(self, value):
        """
        Checks if two integers are not equal.

        Args:
        - value (int): The value to compare with.

        Returns:
        - bool: True if the integers are not equal, False otherwise.
        """
        return self.real != value.real

    def __ne__(self, value):
        """
        Checks if two integers are equal.

        Args:
        - value (int): The value to compare with.

        Returns:
        - bool: True if the integers are equal, False otherwise.
        """
        return self.real == value.real
