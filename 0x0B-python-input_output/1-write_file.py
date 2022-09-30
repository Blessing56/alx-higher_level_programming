#!/usr/bin/python3
"""Defines a function that writes a string to a textfile"""


def write_file(filename="", text=""):
    """Returns the number of characters written
    Args:
        filename(str): the name of the file to be written to
        text(str): the text to be written to the file
    Returns:
        the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as d:
        return (d.write(text))
