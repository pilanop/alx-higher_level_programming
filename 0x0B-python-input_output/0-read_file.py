#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it.

    Args:
        filename: (str) The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
