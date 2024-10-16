#!/usr/bin/python3
"""

Module 6-base_geometry contains:
an empty class called BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """

    Methods:
            area(self)
            integer_validation(self, name, value)
    """
    def area(self):
        """ not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates input
        Args:
            name: assumed always a string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
