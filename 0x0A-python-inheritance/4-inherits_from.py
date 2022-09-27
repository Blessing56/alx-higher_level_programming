#!/usr/bin/python3
"""defining an inherited class method"""


def inherits_from(obj, a_class):
    """
    Checks if the object is  an inherited instance of the class

    Args:
        obj: Object tobe checked
        a_class: the class type to be compared with the object
    Returns:
        True: is the object is an inherited class
        False: otherwise
    """
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
