#!/usr/bin/python3
"""defining a Rectangle"""

class Rectangle:
    """instantiating a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """getter to retrieve the  private attribute width"""
    @property
    def width(self):
        return self.__width
    
    """setter for width"""
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    """getter to retrieve the  private attribute height"""
    @property
    def height(self):
        return self.__height

    """setter for height"""
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise Valueerror("height must be >= 0")
