#!/usr/bin/python3
def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
    text (str): The text to format.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
