#!/usr/bin/python3
"""
A module with a Rectangle class that defines a rectangle.
"""

class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the Rectangle.
            height (int, optional): The height of the Rectangle.
        """
        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The width of the Rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height of the Rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        Validate the width.

        Args:
            width (int): The width to validate.

        Raises:
            TypeError: If `width` is not an int.
            ValueError: If `width` is less than 0.
        """
        if not self.__check_int_value(width):
            raise TypeError('width must be an integer')

        if not self.__check_positive_value(width):
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        Validate the height.

        Args:
            height (int): The height to validate.

        Raises:
            TypeError: If `height` is not an int.
            ValueError: If `height` is less than 0.
        """
        if not self.__check_int_value(height):
            raise TypeError('height must be an integer')

        if not self.__check_positive_value(height):
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        Check if the value is an integer.

        Args:
            value (int): The number to verify.

        Returns:
            bool: True if `value` is an int, False otherwise.
        """
        return isinstance(value, int)

    def __check_positive_value(self, value):
        """
        Check if the value is a positive integer.

        Args:
            value (int): The number to verify.

        Returns:
            bool: True if `value` is greater than or equal to 0, False otherwise.
        """
        return value >= 0
