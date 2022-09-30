#!/usr/bin/python3
"""Defines a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object (python data structure) represented 
    by a JSON string"""

    return json.dumps(my_str)
