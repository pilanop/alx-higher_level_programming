#!/usr/bin/python3
def pascal_triangle(n):
    new_list = [[1]]
    if n <= 0:
        return new_list
    for i in range(n - 1):
        temp = [0] + new_list[-1] + [0]
        new_row = []
        for j in range(len(new_list[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        new_list.append(new_row)
    return new_list
