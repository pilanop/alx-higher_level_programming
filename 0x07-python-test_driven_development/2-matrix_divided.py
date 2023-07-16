#!/usr/bin/python3
"""
This add_integer function performs integer addition of two input values.
It accepts either integers or floats
(which are typecast to integers) as arguments,
and raises a TypeError if any other type of input is given.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a given matrix by a divisor and returns a new
    matrix.

    Args:
        matrix (List[List[int or float]]): The matrix to be divided.
            A matrix represented as a list of lists, where each inner list
            represents a row and contains integers or floats.
        div (int or float): The divisor.
            A number to divide each element of the matrix by.

    Returns:
        List[List[float]]: The new matrix with each element divided by the
        divisor.

    Raises:
        TypeError: If the divisor is not an integer or float.
        TypeError: If division by zero is attempted.
        TypeError: If the matrix is not a valid matrix (list of lists).
        TypeError: If the rows of the matrix do not have the same size.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise TypeError("division by zero")

    new_matrix = []

    r_size = None

    for r in matrix:
        new_r = []

        if r_size is None:
            r_size = len(r)
        elif len(r) != r_size:
            raise TypeError("Each row of the matrix must have the same size")

        for e in r:
            if not isinstance(e, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

            new_e = round((e / div), 2)

            if len(new_r) == len(r):
                break

            new_r.append(new_e)

        new_matrix.append(new_r)

    return new_matrix
