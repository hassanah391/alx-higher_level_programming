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
    instance methods:
    __init__(self, width, height, x=0, y=0, id=None)
    area(self): returns the area value of the Rectangle instance
    desplay: prints in stdout the Rectangle instance with the character '#'
    __str__: returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
The Rectangle class includes public getter and setter methods for each of its
private attributes, ensuring encapsulation and validation where necessary.
"""


from models.base import Base
import json


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
        """ initlizes instance attributes"""
        # Validates height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        # Validates width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        # validates X
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        # Validates Y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id=id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character '#'
        by taking care of x and y"""
        # Print vertical offset (empty lines for y)
        for _ in range(self.y):
            print()

        # Print each row of the rectangle
        for _ in range(self.height):
            # Print horizontal offset (spaces for x)
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def update(self, *args):
        """
    Updates the Rectangle attributes using positional arguments.

    Args:
        *args: Variable length argument list
            - 1st argument represents id
            - 2nd argument represents width
            - 3rd argument represents height
            - 4th argument represents x
            - 5th argument represents y
    """
        # List of attributes in the order they should be updated
        attributies = ["id", "width", "height", "x", "y"]
        # Update each attribute if a corresponding argument was provided
        for i in range(len(args)):
            if i < len(attributies):
                setattr(self, attributies[i], args[i])
