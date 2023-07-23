#!/usr/bin/python3
"""The is_kind_of_class function in Python checks whether a given object
is an instance of a specified class or type and returns a boolean result.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj:
            The object to check the type of.
        a_class:
            The class or type to check against.

    Returns:
        True if the object is an instance of the specified class or type;
        False otherwise.
    """
    return isinstance(obj, a_class)
