#!/usr/bin/python3

"""Defines a function for appending text to a file."""

def add_content_to_file(file_path="", content_to_add=""):
    """Appends a string to the end of a UTF-8 encoded text file.

    Parameters:
        file_path (str): The path to the file where content will be appended.
        content_to_add (str): The text to be appended to the file.
    
    Returns:
        int: The number of characters appended.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        return file.write(content_to_add)
