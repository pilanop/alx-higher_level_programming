#!/usr/bin/python3

"""
Defines a name-printing function.
that prints My name is <first name> <last name>
Prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person. (default: "")

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
