#!/usr/bin/python3
def fizzbuzz():
    for io in range(1, 101):
        if io % 3 == 0 and io % 5 == 0:
            print("FizzBuzz ", end='')
        elif io % 3 == 0:
            print("Fizz ", end='')
        elif io % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(io), end='')
