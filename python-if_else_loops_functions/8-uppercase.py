#!/usr/bin/python3
def convert_to_uppercase(input_string):
    for character in input_string:
        if 'a' <= character <= 'z':
            character = chr(ord(character) - 32)
        print(f"{character}", end="")
    print()
