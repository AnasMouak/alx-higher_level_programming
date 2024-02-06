#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the specified attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a dictionary representation.

        Returns:
            dict: A dictionary containing the attributes of the student object.
        """
        return self.__dict__
