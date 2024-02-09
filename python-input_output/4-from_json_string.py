#!/usr/bin/python3

"""Module for deserializing JSON strings to Python objects."""

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be deserialized.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
