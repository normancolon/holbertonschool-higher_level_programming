#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (any): The object to lookup.

    Returns:
    list: A list of strings, each being an attribute or method name.
    """
    return dir(obj)
