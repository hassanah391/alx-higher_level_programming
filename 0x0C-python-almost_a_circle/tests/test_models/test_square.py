#!/usr/bin/python3
"""

A unit test for Square class, Run these commands:
$ python3 -m unittest discover tests
$ python3 -m unittest tests/test_models/test_square.py
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        obj1 = Square(3, 1, 3)

    def test_str(self):
        obj1 = Square(3, 1, 3, 3)
        self.assertEquals(obj1.__str__(), "[Square] (3) 1/3 - 3")
