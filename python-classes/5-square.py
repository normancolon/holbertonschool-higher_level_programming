#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private instance attribute size, property and property setter for size, and method to print square
"""

class Square:
    """Class Square with method to print square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
