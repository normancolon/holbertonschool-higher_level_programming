#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private instance attribute size and size validation
"""

class Square:
    """Class Square with size validation"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
