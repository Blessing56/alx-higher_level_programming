#!/usr/bin/python3
"""class square inherites afrom the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiating the class square

    Args:
        size(int): size of the square
    """

    def __init__(self, size):
        """calling the integer_validate method
        to validate the integer
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
