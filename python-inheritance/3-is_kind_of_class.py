#!/usr/bin/python3
"""
This module defines the is_kind_of_class function used to check
if an object is an instance of, or if the object is an instance
of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Determines if obj is an instance of a_class or if obj is an instance
    of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if obj is an instance of a_class or if obj is an instance
        of a class that inherited from a_class. False otherwise.
    """
    return isinstance(obj, a_class)
