#!/usr/bin/python3
""" contains the from_json_string function """
import json


def from_json_string(my_str):
    """ returns object represented by json string """
    return json.loads(my_str)
