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
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value=0):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
