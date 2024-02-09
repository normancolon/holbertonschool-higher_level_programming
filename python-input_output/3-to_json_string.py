#!/usr/bin/python3

"""Module to convert Python objects to JSON strings."""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Parameters:
    - my_obj: The Python object to convert to a JSON string.

    Returns:
    A string containing the JSON representation of my_obj.
    """
    return json.dumps(my_obj)

