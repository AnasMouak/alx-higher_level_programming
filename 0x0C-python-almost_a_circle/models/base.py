#!/usr/bin/python3
"""Defines a base class for managing object IDs."""

import json
import csv
import os

class Base:
    """Represents a base class for managing object IDs."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique ID.

        Args:
        - id (int, optional): The ID to assign to the instance.
        If not provided, a unique ID is generated.

        Returns:
        - None
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted
            to JSON.

        Returns:
            str: A string representing the list of dictionaries in JSON format.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be saved to the file.

        Returns:
            None
        """
        if list_objs is None:
           list_objs = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            n = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(n)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted to a list of
            dictionaries.

        Returns:
            list: A list containing dictionaries parsed from the JSON string.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class from a dictionary.

        Args:
            **dictionary (dict): Keyword arguments used to initialize
            the object.

        Returns:
            Instance: An instance of the class initialized with the dictionary
            values.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file and create instances of the class.

        Args:
            None

        Returns:
            list: A list containing instances of the class loaded from
            the JSON file.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename,  encoding="utf-8") as f:
            n = cls.from_json_string(f.read())
            return [cls.create(**i) for i in n]
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to be saved to the file.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file and create instances of the class.

        Args:
            None

        Returns:
            list: A list containing instances of the class loaded from
            the CSV file.
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            n = csv.DictReader(f, fieldnames=fieldnames)
            n = [dict([k, int(v)] for k, v in d.items()) for d in n]
            return [cls.create(**i) for i in n]
