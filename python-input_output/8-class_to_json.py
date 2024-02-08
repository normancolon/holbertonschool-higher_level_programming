#!/usr/bin/python3
""" contains the load_from_json_file function """
import json


def load_from_json_file(fname):
    """ creates an obj from a json file """
    with open(fname, encoding='utf-8') as f:
        return json.load(f)
