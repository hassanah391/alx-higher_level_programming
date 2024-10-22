#!/usr/bin/python3
"""

Module rectangle defines Rectangle class that inheriting form The Base class:

Class:
Rectangle:
    A class representing a rectangle, inheriting from the Base class.

Attributes:
    -__width -> width
    -__height -> height
    -__x -> x
    -__y -> y

Methods:
    __init__(self, width, height, x=0, y=0, id=None)

The Rectangle class includes public getter and setter methods for each of its
private attributes, ensuring encapsulation and validation where necessary.
"""


from models.base import Base


class Rectangle(Base):
    """
    Attributes:
        private instance:
            -__width -> width: for width of the rectangle
            -__height -> height: for height of the rectangle
            -__x -> x: for the x-coordinate of the rectangle
            -__y -> y: for the y-coordinate of the rectangle.
    Methods:
        private instance:
            __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id=id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not value > 0:
            raise ValueError("Width should be a positive number")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not value > 0:
            raise ValueError("height should be a positive number")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not value > 0:
            raise ValueError("X should be a positive number")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not value > 0:
            raise ValueError("Y should be a positive number")
        else:
            self.__y = value
