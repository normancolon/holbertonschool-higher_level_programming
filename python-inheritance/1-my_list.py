#!/usr/bin/python3
"""
A class MyList that inherits from list.
This module demonstrates a custom list with the ability to print itself in sorted order.
"""

class MyList(list):
    """
    A subclass of list with an added method to print the list in ascending order.
    
    The class overrides no methods from the list class but adds `print_sorted`.
    This method does not modify the original list but prints a sorted version of it.
    """
    
    def print_sorted(self):
        """Prints the list elements in ascending order without modifying the original list."""
        print(sorted(self))
