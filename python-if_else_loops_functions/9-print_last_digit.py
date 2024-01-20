#!/usr/bin/python3
def display_final_digit(num):
    final_digit = abs(num) % 10
    print(final_digit, end="")
    return final_digit
