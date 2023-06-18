#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        m = list(map(lambda num: num ** 2, i))
        new_matrix.append(m)

    return new_matrix
