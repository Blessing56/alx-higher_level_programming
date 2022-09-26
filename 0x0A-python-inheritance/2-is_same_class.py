#!/usr/bin/python3
"""Defining a function"""


def is_same_class(obj, a_class):
    """Checking if a class is an instance of another class"""
    if type(obj) == a_class:
        return True
    return False
