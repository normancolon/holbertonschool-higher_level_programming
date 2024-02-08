#!/usr/bin/python3
"""
Module 9-rectangle.py with class Rectangle inheriting from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry and represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
