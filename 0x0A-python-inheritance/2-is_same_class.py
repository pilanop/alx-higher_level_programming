#!/usr/bin/python3
"""The function checks if an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Description:
        Check if the type of object matches the specified class.
    Args:
        obj:
            The object to be checked.
        a_class:
            The class to be compared with.
    Returns:
        bool:
            True if the type of the object matches the specified class.
            False otherwise.
    """
    return type(obj) is a_class
