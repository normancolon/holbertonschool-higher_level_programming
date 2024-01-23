#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    x = 10
    y = 5
    print("{:d} + {:d} = {:d}".format(x, y, add(x, y)))
    print("{:d} - {:d} = {:d}".format(x, y, sub(x, y)))
    print("{:d} * {:d} = {:d}".format(x, y, mul(x, y)))
    print("{:d} / {:d} = {:d}".format(x, y, div(x, y)))

