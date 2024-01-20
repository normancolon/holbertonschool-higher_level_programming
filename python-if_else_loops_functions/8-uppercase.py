# Function to print a string in uppercase
def uppercase(string):
    for char in string:
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print(upper_char, end="")
    print()