#!/usr/bin/python3
"""
Defines a function that converts a Python object to a JSON-formatted string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str: A JSON string to be converted to a Python object.

    Returns:
        The Python object representation of the JSON string.
    """
    return json.loads(my_str)
