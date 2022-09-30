#!/usr/bin/python3
"""Defines a function that appends a string to the end of a textfile"""


def append_write(filename="", text=""):
    """Returns the number of characters written
    Args:
        filename(str): the name of the file to be appended to
        text(str): the text to be appended to the file
    Returns:
        the number of characters added
    """

    with open(filename, "a", encoding="utf-8") as d:
        return (d.write(text))
