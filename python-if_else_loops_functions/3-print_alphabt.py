# This script prints the lowercase alphabet excluding 'q' and 'e'
print("".join(chr(letter) for letter in range(ord('a'), ord('z')+1) if letter not in [ord('q'), ord('e')]), end="")