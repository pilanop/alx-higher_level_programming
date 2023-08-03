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
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding="utf8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
