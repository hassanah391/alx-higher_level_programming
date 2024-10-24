#!/usr/bin/python3
"""

Module square contains:

Class:
Square:
    A class representing a square that inherits from class Rectangle
    in module rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class representing a square that inherits from class Rectangle
    in module rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """ initlizes instance attributes"""
        # inherits Rectangle attributes
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
