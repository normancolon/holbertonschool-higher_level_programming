#!/usr/bin/python3
for io in range(0, 10):
    for j in range(io + 1, 10):
        if io == 8 and j == 9:
            print("{}{}".format(io, j))
        else:
            print("{}{}".format(io, j), end=', ')
