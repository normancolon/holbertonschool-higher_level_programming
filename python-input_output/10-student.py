#!/usr/bin/python3
""" contains the  class_to_json function """


def class_to_json(obj):
    """ returns dict description for JSON obj """
    return obj.__dict__
