#!/usr/bin/python3

"""Defines a function for converting JSON strings to Python objects."""
import json

def json_to_object(json_string):
    """
    Converts a JSON string to a Python object.

    Parameters:
        json_string (str): The JSON string to be converted.
    
    Returns:
        The Python object representation of the JSON string.
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
