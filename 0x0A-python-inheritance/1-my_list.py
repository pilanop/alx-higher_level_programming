#!/usr/bin/python3
"""
inherits from the built-in list class and adds a method print_sorted
"""


class MyList(list):
    """A class representing a custom list.
    """
    def print_sorted(self):
        """
        Sorts the elements of the list and prints them.
        """
        print(sorted(self))
