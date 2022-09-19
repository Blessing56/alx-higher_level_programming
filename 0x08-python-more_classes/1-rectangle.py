#!/usr/bin/python3
"""defining a Rectangle"""


class Rectangle:
    """instantiating a rectangle
    Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """getter to retrieve the  private attribute width"""
    @property
    def width(self):
        return self.__width

    """setter for width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """getter to retrieve the  private attribute height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise Valueerror("height must be >= 0")
        self.__height = value
