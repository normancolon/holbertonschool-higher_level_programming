#!/usr/bin/python3
for io in range(0, 100):
    if io != 99:
        print("{:02d}, ".format(io), end='')
    else:
        print("{:02d}".format(io))
