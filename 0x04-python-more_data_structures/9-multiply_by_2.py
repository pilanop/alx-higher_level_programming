#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    my_list = []
    for key in a_dictionary.items():
        values = list(key)
        values[1] *= 2
        my_list.append(tuple(values))
        my_dict = dict(my_list)
    return my_dict
