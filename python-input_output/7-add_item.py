#!/usr/bin/python3
""" contains the save_to_json_file function """
import json


def save_to_json_file(my_obj, fname):
    """ writes an obj to a text file, using json representation """
    with open(fname, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
