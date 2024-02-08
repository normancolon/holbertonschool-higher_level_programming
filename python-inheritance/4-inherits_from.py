#!/usr/bin/python3
"""
This module defines the inherits_from function that checks
if an object is an instance of a class that inherited (directly or
indirectly) from the specified class, excluding objects that are
direct instances of the specified class.
"""

def inherits_from(obj, a_class):
    """
    Determine if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        excluding direct instances of a_class. False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
