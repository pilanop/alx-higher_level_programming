#!/usr/bin/python3
"""This Python function checks if the given object is an instance of a
subclass of the specified class,
returning True if it is and False otherwise.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: An object whose inheritance is to be checked.
        a_class: A class to check if the object inherits from.

    Returns:
        True if the object inherits from the given class, False otherwise.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
