#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Args:
    - my_list (list, optional): Initial list to initialize the MyList.
    Default is an empty list.

    Methods:
    - print_sorted(self): Prints the elements of the list in sorted order.
    """

    def __init__(self, my_list=[]):
        super().__init__(my_list)

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Returns:
        - None
        """
        print(sorted(self))
