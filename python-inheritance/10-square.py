#!/usr/bin/python3
"""
Module 10-square.py with class Square inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides, must be a positive integer.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

