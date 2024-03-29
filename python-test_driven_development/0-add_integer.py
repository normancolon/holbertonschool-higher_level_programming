#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers, a and b.

    Args:
    a (int or float): The first number.
    b (int or float): The second number (defaults to 98).

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
