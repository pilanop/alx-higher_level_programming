#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        y = (0, 0)
        tuple_a += y
    elif len(tuple_a) < 2:
        y = (0,)
        tuple_a += y

    if len(tuple_b) == 0:
        y = (0, 0)
        tuple_b += y
    elif len(tuple_b) < 2:
        x = (0,)
        tuple_b += x

    new_tuple = (
        tuple_a[0] + tuple_b[0],
        tuple_a[1] + tuple_b[1]
    )
    return new_tuple
