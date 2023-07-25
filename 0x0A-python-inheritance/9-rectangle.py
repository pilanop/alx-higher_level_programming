#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle object.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Args:
            width: The width of the rectangle. (int)
            height: The height of the rectangle. (int)
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the geometry.
        Raises:
            Exception: If the `area()` method is not implemented.
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
