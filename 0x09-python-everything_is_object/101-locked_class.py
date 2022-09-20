#!/usr/bin/python3

"""Defining a Locked Class"""


class LockedClass:
    """
    Preventing the user fron dynamically creating new instance attributes, except if the new instance atttribute is called first_name
    """
    __slots__ = ["first_name"]
    def __init__(self):
        pass
