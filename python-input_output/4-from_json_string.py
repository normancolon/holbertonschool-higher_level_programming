#!/usr/bin/python3
""" contains the append_write function """


def append_write(fname="", text=""):
    """ appends a string to end of text file and return num of char written"""
    with open(fname, 'a', encoding='utf-8') as f:
        return f.write(text)
