#!/usr/bin/python3
"""
Module 7-base_geometry.py with class BaseGeometry including method integer_validator.
"""

class BaseGeometry:
    """
    A class with public instance methods area and integer_validator.
    """

    def area(self):
        """
        Raises an Exception with the message that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
