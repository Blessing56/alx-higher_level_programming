#!/usr/bin/python3
"""Rectangle inherites the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantaiating the class Rectangle

    Args:

    width: withd of the rectangle
    height: height of cthe rectangle

    """

    def __init__(self, width, height):
        """calling the integer_validate method
        to validate the integer
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        r = f"[Rectangle] {self.__width}/{self.__height}"
        return r
