#!/usr/bin/python3
"""Defines a function that converts a Python object to a JSON-formatted string.
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON-formatted string representation of the Python object.
    """
    return json.dumps(my_obj)
