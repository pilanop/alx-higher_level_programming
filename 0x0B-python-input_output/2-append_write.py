#!/usr/bin/python3
"""Appends and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str): The name of the file to append the text to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
