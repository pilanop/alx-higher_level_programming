#!/usr/bin/python3
"""writes and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes the provided text to a file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The total number of characters written to the file.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
        return f.tell()
