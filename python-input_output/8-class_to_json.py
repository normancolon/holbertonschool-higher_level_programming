#!/usr/bin/python3

"""Defines a function to convert class instances to JSON-compatible dict."""

def instance_to_dict(instance):
    """Converts a class instance into a dictionary representing its attributes.

    Parameters:
        instance: The instance of the class to be converted into a dict.

    Returns:
        dict: A dictionary containing all attributes of the instance.
    """
    return instance.__dict__
