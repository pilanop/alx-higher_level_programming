#!/usr/bin/python3
"""
Defines a function that writes an Object to a text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves the given object to a JSON file.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
