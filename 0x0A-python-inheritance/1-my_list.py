#!/usr/bin/python3
"""MyList inherites a class list"""


class MyList(list):
        """Instantiates the subclass"""
        def __init__(self):
            """Initializes the object"""
            super().__init__()

        def print_sorted(self):
            """prints the sorted list"""
            print(sorted(self))
