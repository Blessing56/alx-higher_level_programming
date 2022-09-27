#!/usr/bin/python3
"""Defining a class BaseGeometry"""


class BaseGeometry:
    """definfig a class method"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method thatValidates value
        Args:
            name: a string attribute
            value: value attribute
        """

        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

