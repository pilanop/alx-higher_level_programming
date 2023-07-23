#!/usr/bin/python3
"""
This Python function defines a class MyList that inherits
from the built-in list class and adds a method print_sorted to sort
and print the elements of the list in ascending order.
"""


class MyList(list):
    """A class representing a custom list.
    """

    def print_sorted(self):
        """
        Sorts the elements of the list in ascending order and prints them.
        """
        print(sorted(self))
