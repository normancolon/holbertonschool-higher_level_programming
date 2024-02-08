#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

# This part below is not part of the function but demonstrates how to use it.
# Assuming the existence of '0-main.py' as described and 'my_file_0.txt'
if __name__ == "__main__":
    read_file("my_file_0.txt")
