#!/usr/bin/python3
"""
Defines a class Base
"""


class Base:
    """
    A class representing a base object.

    Attributes:
        __nb_objects (int): The number of base objects created.

    Methods:
        __init__(self, id=None): Initializes a new base object.
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
