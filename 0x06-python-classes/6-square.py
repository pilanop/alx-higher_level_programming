#!/usr/bin/python3
"""
A class `Square` that defines a square
"""


class Square:
    """
    Square class

    This class represents a square. It has properties such as size and
    position, and methods to calculate the area and print the square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args: size (int, optional): The size of the square. Default is 0.
        position (tuple, optional): The position of the square. Default is (
        0, 0).
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the Square object.

        Returns: A tuple representing the position of the Square. The tuple
        contains two integers representing the x and y coordinates of the
        Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args: value: A tuple of 2 positive integers representing the x and y
        coordinates of the position.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.

        """
        error_message = "position must be a tuple of 2 positive integers"
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError(error_message)

        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError(error_message)

        self.__position = value

    def area(self):
        """
        Calculates the area of a square.

        Returns:
                int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints a square of '#' characters with a specified size and position.

        Parameters:
            self (Square): The Square instance.

        Returns:
            None
        """
        for _ in range(self.__position[1] if self.__size else 1):
            print()

        print(
            "\n".join(
                [
                    " " * self.__position[0] + "#" * self.__size
                    for _ in range(self.__size)
                ]
            )
        )
