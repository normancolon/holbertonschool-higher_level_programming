#!/usr/bin/python3
import sys

# Assuming 'save_to_json_file' and 'load_from_json_file' are defined in the files
# '5-save_to_json_file.py' and '6-load_from_json_file.py' respectively
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load existing items from the file. If the file doesn't exist, start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command-line arguments to the list, skipping the first argument which is the script name itself
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
