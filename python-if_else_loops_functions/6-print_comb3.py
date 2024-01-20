#!/usr/bin/python3
# First loop for the first digit
for first_digit in range(0, 9):
    # Second loop for the second digit
    for second_digit in range(first_digit + 1, 10):
        if first_digit < second_digit:
            if first_digit != 8 or second_digit != 9:
                print(f"{first_digit}{second_digit}", end=", ")
            else:
                print(f"{first_digit}{second_digit}")
