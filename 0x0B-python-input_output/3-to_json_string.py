#!/usr/bin/python3
"""Defines a JSON function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj(str): string object
    Returns:
        The representation of the object
    """

    return json.dumps(my_obj)
