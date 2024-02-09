#!/usr/bin/python3

"""Aggregates command-line arguments into a list and saves to a JSON file."""
import sys

if __name__ == "__main__":
    # Importing functions with aliases for clarity
    json_saver = __import__('5-save_to_json_file').save_to_json_file
    json_loader = __import__('6-load_from_json_file').load_from_json_file

    # File to store the aggregated items
    target_file = "add_item.json"

    try:
        # Attempt to load existing content from the file
        aggregated_list = json_loader(target_file)
    except FileNotFoundError:
        # Initialize an empty list if the file does not exist
        aggregated_list = []

    # Extend the list with command-line arguments (excluding the script name)
    aggregated_list.extend(sys.argv[1:])

    # Save the updated list back to the file
    json_saver(aggregated_list, target_file)
