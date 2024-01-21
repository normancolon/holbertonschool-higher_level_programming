#!/usr/bin/python3
for io in range(0, 90):
    if io % 10 > io / 10:
        if io != 89:
            print("{:02d}, ".format(i), end='')
        else:
            print("{:02d}".format(i))
