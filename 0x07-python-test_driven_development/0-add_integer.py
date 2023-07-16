#!/usr/bin/python3
"""
This add_integer function performs integer addition of two input values.
It accepts either integers or floats (which are typecast to integers) as
arguments, and raises a TypeError if any other type of input is given.
"""


def add_integer(a, b=98):
    """
    Args: a: An integer or float value for addition. b: An optional integer
    or float value for addition. Defaults to 98 if not provided.

    Returns:
            The sum of `a` and `b`, both converted to integers.

    Raises:
            TypeError: If either `a` or `b` is not an integer or float value.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
