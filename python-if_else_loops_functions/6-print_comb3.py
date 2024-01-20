#!/usr/bin/python3
print(", ".join(f"{digit1}{digit2}" for digit1 in range(10) for digit2 in range(digit1 + 1, 10)))
