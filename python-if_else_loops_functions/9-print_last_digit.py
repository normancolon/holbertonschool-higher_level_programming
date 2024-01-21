#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        new_number = num * -1
        last_digit = (-1) * (new_num % 10)
        last_digit = last_digit * -1
    else:
        last_digit = num % 10

    print("{:d}".format(last_digit), end='')
    return last_digit
