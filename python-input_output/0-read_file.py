#!/usr/bin/env python3
"""Enhanced file reader module."""

def display_text_content(file_path=""):
    """
    This function opens and displays the content of a specified text file.
    
    """
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            for content_line in file:
                # Strip the newline character for consistent spacing.
                print(content_line.rstrip('\n'))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
