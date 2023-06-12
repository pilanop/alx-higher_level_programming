#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for element in row:
                print("{}".format(element), end=" ")
            print()
