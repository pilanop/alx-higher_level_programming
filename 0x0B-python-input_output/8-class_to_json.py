#!/usr/bin/python3
"""defines a function that returns the dictionary description with simple data
"""


def class_to_json(obj):
    """
    Converts a class object to a JSON string.

    Args:
        obj: The class object to be converted.

    Returns:
        str: The JSON string representing the class object.
    """
    return obj.__dict__
