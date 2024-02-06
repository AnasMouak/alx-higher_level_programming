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

    def to_json(self, attrs=None):
        """
        Converts the student object to a dictionary representation.

        Args:
            attrs (list of str, optional): A list of attribute names
            to retrieve.

        Returns:
            dict: A dictionary containing the attributes of the student object.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str)
                                           for ele in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the object's attributes based on the provided JSON dictionary.

        Args:
        json (dict): A dictionary containing attribute-value pairs to update.

        Returns:
            None
        """
        for key, val in json.items():
            setattr(self, key, val)
