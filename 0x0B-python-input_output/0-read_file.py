#!/usr/bin/python3
"""Defines a file  that reads text"""


def read_file(filename=""):
    """Prints the contents of the file to stdout"""
    with open(filename, encoding="utf-8") as d:
        print(d.read(), end='')
