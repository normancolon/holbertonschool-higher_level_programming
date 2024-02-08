#!/usr/bin/python3
""" write_file function """


def write_file(fname="", text=""):
    """ write a string to a text file and return num of char """
    with open(fname, 'w', encoding='utf-8') as f:
        return f.write(text)
