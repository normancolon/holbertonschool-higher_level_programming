#!/usr/bin/python3
"A module for looking up attributes and methods of an object."

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object for which to list attributes and methods.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)

