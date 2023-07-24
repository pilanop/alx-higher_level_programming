#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Calculate the area of the geometry object.

    Not implemented by subclasses to calculate the
    area of the geometry object.

    Raises:
        Exception: that area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
