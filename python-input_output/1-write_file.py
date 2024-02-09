#!/usr/bin/python3

"""Defines a function for writing to a file."""

def save_text_to_file(file_path="", content=""):
    """Save a string to a UTF-8 encoded text file.

    Parameters:
        file_path (str): The path to the file where the content will be saved.
        content (str): The content to save in the file.
    
    Returns:
        int: The number of characters saved.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        return file.write(content)
