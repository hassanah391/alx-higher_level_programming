#!/usr/bin/python3
"""

Module 6-load_from_json_file contains:

load_from_json_file: a function that creates an Object from a “JSON file”
"""
from json import load


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return load(f)
