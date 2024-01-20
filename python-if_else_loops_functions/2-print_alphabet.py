#!/usr/bin/python3

# Looping through the lowercase alphabet using character conversion
for letter in (chr(x) for x in range(ord('a'), ord('z') + 1)):
    print(letter, end='')
