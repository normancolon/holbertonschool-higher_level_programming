#!/usr/bin/python3
print("".join(chr(letter) for letter in range(ord('a'), ord('z')+1) if letter not in [ord('q'), ord('e')]), end="")
