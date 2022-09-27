#!/usr/bin/python3
"""Defining a class MyList"""


class MyList(list):
        """Defining the class methods"""
        def print_sorted(self):
            print(sorted(self))
