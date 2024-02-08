#!/usr/bin/python3
"""
A class MyList that inherits from list.
This module provides a subclass of the built-in list with additional functionality.
"""

class MyList(list):
    """
    A subclass of list that includes a method to print the list in sorted order.

    Methods:
    - print_sorted: Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """Prints the list elements in ascending order without modifying the original list."""
        print(sorted(self))
