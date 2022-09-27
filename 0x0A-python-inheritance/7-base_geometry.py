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

