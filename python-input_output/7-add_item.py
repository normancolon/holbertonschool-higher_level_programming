#!/usr/bin/python3

"""Aggregates all command-line arguments into a list and stores it in a JSON file."""
import sys
import importlib.util

def main():
    filename = "collected_args.json"

    # Dynamically import 'save_to_json_file' function
    save_module_name = '5-save_to_json_file'
    save_module_spec = importlib.util.spec_from_file_location(save_module_name, f"./{save_module_name}.py")
    save_module = importlib.util.module_from_spec(save_module_spec)
    save_module_spec.loader.exec_module(save_module)

    # Dynamically import 'load_from_json_file' function
    load_module_name = '6-load_from_json_file'
    load_module_spec = importlib.util.spec_from_file_location(load_module_name, f"./{load_module_name}.py")
    load_module = importlib.util.module_from_spec(load_module_spec)
    load_module_spec.loader.exec_module(load_module)

    try:
        # Attempt to load existing list from the file
        items = load_module.load_from_json_file(filename)
    except FileNotFoundError:
        # Initialize an empty list if file does not exist
        items = []

    # Extend the list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_module.save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
