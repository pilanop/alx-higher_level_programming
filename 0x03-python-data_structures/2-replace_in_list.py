#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    new_list = my_list
    new_list[idx] = element
    if idx < 0 or idx > length:
        return my_list
    else:
        return new_list
