#!/usr/bin/python3
"""

Module 10-square contains:

super class BaseGeometry:
with public instance method area and integer_validation

subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__

subclass Square
with instantiation of private attribute size, validated by superclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
    __init__(self, size)
    """
    def __init__(self, size):
        """ initializes size
        Args:
            size(int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            return f"[Square] {self.__size}/{self.__size}"
