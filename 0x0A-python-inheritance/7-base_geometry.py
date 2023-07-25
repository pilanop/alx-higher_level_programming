#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """
    Class representing a base geometry.
    """
    def area(self):
        """Calculates the area of the geometry.
        Raises:
            Exception: If the `area()` method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
            name (str): The name of the variable being validated.
            value (int): The value of the variable being validated.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
