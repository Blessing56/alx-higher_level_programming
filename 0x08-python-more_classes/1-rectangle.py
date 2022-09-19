#!/usr/bin/python3
"""Creates a Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the  private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the  private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise Valueerror("height must be >= 0")
        self.__height = value
