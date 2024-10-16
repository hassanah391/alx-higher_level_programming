#!/usr/bin/python3
"""
Module 2-is_same_class contains:
 a function called is_same_class that returns True if the object is exactly
 an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Return:
    true if obj an instance of a_class
    otherwise retuen false
    """
    return type(obj) == a_class
