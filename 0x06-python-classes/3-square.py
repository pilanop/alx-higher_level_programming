#!/usr/bin/python3
"""
A class `Square` that defines a square by: (based on /2-square.py)
"""


class Square:
    """
    A class representing a square.

    Attributes:
            __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
                size (int): The size of the square. Defaults to 0.

        Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of a square.

        Returns:
                float: The area of the square.
        """
        return self.__size**2

    pass
