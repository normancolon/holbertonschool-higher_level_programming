#!/usr/bin/python3

"""Defines a function for saving objects to files in JSON format."""
import json

def write_json_to_file(object_to_save, file_path):
    """Saves a Python object to a file using its JSON string representation.

    Parameters:
        object_to_save: The Python object to be saved.
        file_path (str): The path to the file where the object will be saved in JSON format.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(object_to_save, file)
