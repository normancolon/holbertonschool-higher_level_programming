#!/usr/bin/python3
"""  the read_lines function """


def read_lines(fname="", nb_lines=0):
    """ reads a n lines of a text file and prints them   """
    count = 0
    with open(fname, encoding='utf-8') as f:
        for line in f:
            count += 1
        f.seek(0)
        if 0 < nb_lines < count:
            for i in range(nb_lines):
                print(f.readline(), end="")
                i += 1
        else:
            for line in f:
                print(line, end="")
