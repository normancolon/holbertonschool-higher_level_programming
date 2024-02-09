#!/usr/bin/python3

"""Defines a function for converting objects to JSON strings."""
import json

def convert_to_json(obj_to_convert):
    """Returns the JSON string representation of an object.

    Parameters:
        obj_to_convert: The object to be converted into a JSON string.
    
    Returns:
        str: A JSON string representation of the input object.
    """
    return json.dumps(obj_to_convert)

