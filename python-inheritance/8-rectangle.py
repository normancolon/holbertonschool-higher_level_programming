#!/usr/bin/python3
"""
Module 8-rectangle.py with class Rectangle inheriting from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry and represents a rectangle.

    Attributes:
        width (int): The width of the rectangle, must be a positive integer.
        height (int): The height of the rectangle, must be a positive integer.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle, must be a positive integer.
            height (int): The height of the rectangle, must be a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
