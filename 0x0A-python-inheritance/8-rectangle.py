#!/usr/bin/python3
"""Defining a class BaseGeometry"""


class BaseGeometry:
    """definfig a class method"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a parameter as an integer

        Args:
            name: a string attribute
            value: value attribute
        Raises:
            TypeError: If value not an integer
            ValueError: If value is <= 0
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Rectangle inherites the class BaseGeometry"""
class Rectangle(BaseGeometry):
    """Instantaiating the class Rectangle

    Args:
        width: withd of the rectangle
        height: height of cthe rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator(width, height)
