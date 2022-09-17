#!/usr/bin/python3

'''Defines a class Square'''


class Square:
    '''Instantiating the class'''

    def __init__(self, size=0):
        '''
        Arg:
            size(int): size of square.
        '''
        self.size = size

    @property
    def size(self):
        '''getter'''
        return (self.__size)

    @size.setter
    def size(self, value):
        ''' setter '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''returns the current square area'''
        return (self.__size ** 2)
