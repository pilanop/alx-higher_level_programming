#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    new_list = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        temp = [0] + new_list[-1] + [0]
        new_row = []
        for j in range(len(new_list[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        new_list.append(new_row)
    return new_list
