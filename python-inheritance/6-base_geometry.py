#!/usr/bin/python3
"""
Defines a class BaseGeometry with a public instance method.
"""

class BaseGeometry:
    """
    A class with a method that raises an exception.
    """

    def area(self):
        """
        Raises an Exception with a message indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")
