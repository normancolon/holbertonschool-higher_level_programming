#!/usr/bin/python3
"""
Module 11-square.py: Defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle, with size validation and
    a customized string representation.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square sides, validated to be a positive integer.
        """
        super().integer_validator("size", size)  # Validate size using inherited method
        super().__init__(size, size)  # Initialize Rectangle with width and height as size
        self.__size = size  # Private attribute

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Provides a customized string representation of the Square.

        Returns:
            A string in the format [Square] <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"

