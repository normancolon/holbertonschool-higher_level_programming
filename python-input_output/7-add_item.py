#!/usr/bin/python3

"""Aggregates all command-line arguments into a list and stores it in a JSON file."""
import sys

if __name__ == "__main__":
    write_list_to_json = __import__('5-save_to_json_file').save_to_json_file
    read_list_from_json = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        aggregated_items = read_list_from_json("collected_args.json")
    except FileNotFoundError:
        aggregated_items = []
    aggregated_items.extend(sys.argv[1:])
    write_list_to_json(aggregated_items, "collected_args.json")
