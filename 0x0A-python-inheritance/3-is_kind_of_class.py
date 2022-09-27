#!/usr/bin/python3
"""defining a class method"""


def is_kind_of_class(obj, a_class):
    """checking if the object is an instance of the class"""
    if isinstance(obj, a_class):
        return True
    return False
