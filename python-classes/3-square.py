#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private instance attribute size and public instance method to calculate area
"""

class Square:
    """Class Square with method to calculate area"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
