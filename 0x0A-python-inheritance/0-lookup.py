#!/usr/bin/python3
"""
The function lookup(obj) returns a list of all attributes and methods
that can be accessed on the provided Python object 'obj'.
"""


def lookup(obj):
    """
    Args:
        obj: Any object for which the method lookup needs to be performed.

    Returns:
        List[str]: A list of strings containing the names of all methods
        and attributes that can be accessed on the given object.
    """
    return dir(obj)
