#!/usr/bin/python3

def print_reversed_list_integer(ls=[]):

    if ls:

        # point i to the last element
        i = len(ls) - 1

        while i >= 0:
            print("{:d}".format(ls[i]))
            i -= 1
