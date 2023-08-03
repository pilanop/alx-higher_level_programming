#!/usr/bin/python3
"""
Defines a class Base
"""

import json


class Base:
    """
    A class representing a base object.

    Attributes:
        __nb_objects (int): The number of base objects created.

    Methods:
        __init__(self, id=None): Initialize a new base object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class.

        Args:
            id (optional): An identifier for the object. Defaults to None.

        Raises:
            None.

        Returns:
            None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list[dict]): A list of dictionaries to be
            converted to a JSON string.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This class method saves a list of objects to a JSON file.
        Args:
            list_objs: A list of objects to be saved to a file.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding="utf8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string into a Python object.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            object: The Python object representing the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class using the provided dictionary.

        Args:
            **dictionary: A dictionary containing the parameters for creating
                    the instance.

        Returns:
            The newly created instance.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
