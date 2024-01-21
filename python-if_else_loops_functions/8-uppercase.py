#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for io in str:
        if io >= 'a' and io <= 'z':
            new_str = new_str + chr((ord(io) - 32))
        else:
            new_str = new_str + io

    print("{}".format(new_str))
