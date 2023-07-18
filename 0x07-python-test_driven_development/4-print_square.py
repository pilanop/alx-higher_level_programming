#!/usr/bin/python3
"""
Defines a square-printing function.
A function that prints a square with the character '#'.
"""


def print_square(size):
    """
    Prints a square of a given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
