#!/usr/bin/python3

"""Defines a function for loading objects from JSON files."""
import json

def load_from_json_file(file_path):
    """Generates a Python object from a JSON file's content.

    Parameters:
        file_path (str): The path to the JSON file to be read.
    
    Returns:
        The Python object represented by the JSON file content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
