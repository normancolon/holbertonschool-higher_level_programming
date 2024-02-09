#!/usr/bin/python3

"""Aggregates all command-line arguments into a list and stores it in a JSON file."""
import sys

def main():
    # Import the functions directly with their expected names
    from 5-save_to_json_file import save_to_json_file
    from 6-load_from_json_file import load_from_json_file

    filename = "collected_args.json"  # Use the filename from the task instructions

    try:
        # Attempt to load existing list from the file
        items = load_from_json_file(filename)
    except FileNotFoundError:
        # Initialize an empty list if file does not exist
        items = []

    # Extend the list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
