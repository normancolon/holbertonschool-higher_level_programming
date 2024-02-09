#!/usr/bin/python3

"""Defines a function to serialize class instances to JSON-compatible dictionaries."""

def class_to_json(instance):
    """Serializes a class instance to a dictionary that is JSON-compatible.

    Args:
        instance (object): An instance of a class.

    Returns:
        dict: A dictionary representation of the instance suitable for JSON serialization.
    """
    return instance.__dict__
