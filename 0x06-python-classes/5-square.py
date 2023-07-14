#!/usr/bin/python3
"""
A class `Square` that defines a square by: (based on /2-square.py)
"""


class Square:
    """
    Class Square

    Represents a square with a given size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Args:
            size: The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns the size of the Square object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value: An integer representing the size of the square.

        Returns:
            None

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of a square.

        Returns:
                float: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints a square of '#' characters of size self.__size.

        Parameters:
            self: The instance of the Square class.

        Returns:
            None
        """
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

    pass
