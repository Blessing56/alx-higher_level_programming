#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
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
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """return the string rep of rectangle"""
        rect_str = ""
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += str(self.print_symbol)

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __repr__(self):
        """return a formal representation of rectangles"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """display when deleting a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """to return the bigger of the two rectangles
        Args:
            rect_1: one rectangle
            rect_2: another rectangle
        Raises:
            TypeError: if rect_1 or rect_2 are not rectangles
        Returns:
            rectangle  with the greater area or recr_1 if equal
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
