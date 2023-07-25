#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from Rectangle class and defines
    a square with a given size.
    """
    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
