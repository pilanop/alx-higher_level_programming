#!/usr/bin/python3
"""
Defines a function that loads data from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The deserialized JSON data.

    """
    with open(filename, mode='r', encoding='utf8') as f:
        file = f.read()
        return json.loads(file)
