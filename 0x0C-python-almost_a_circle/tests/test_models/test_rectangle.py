#!/usr/bin/python3
"""

A unit test for rectangle class, Run one of these commands:
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_rectangle.py
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_atrributes(self):
        Rec = Rectangle(10, 20, 1, 2)
        self.assertEqual(Rec.width, 10)
        self.assertEqual(Rec.height, 20)
        self.assertEqual(Rec.x, 1)
        self.assertEqual(Rec.y, 2)

    def test_setters(self):
        Rec = Rectangle(10, 20)
        Rec.width = 3000
        Rec.height = 4000
        Rec.x = 3
        Rec.y = 4
        self.assertEqual(Rec.width, 3000)
        self.assertEqual(Rec.height, 4000)
        self.assertEqual(Rec.x, 3)
        self.assertEqual(Rec.y, 4)

    def test_exceptions_atrributes(self):

        Rec = Rectangle(10, 20)
        # test TypeError exception
        with self.assertRaises(TypeError):
            Rec.height = "string"
        with self.assertRaises(TypeError):
            Rec.width = "string"
        with self.assertRaises(TypeError):
            Rec.x = "string"
        with self.assertRaises(TypeError):
            Rec.y = "string"
        # test ValueError exception
        with self.assertRaises(ValueError):
            Rec.height = 0
        with self.assertRaises(ValueError):
            Rec.width = -100
        with self.assertRaises(ValueError):
            Rec.x = -1
        with self.assertRaises(ValueError):
            Rec.y = -2

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        r1 = Rectangle(2, 4, 5, 10, 1001)
        self.assertEqual(r1.__str__(), "[Rectangle] (1001) 5/10 - 2/4")
        r2 = Rectangle(5, 5, 1, id=7)
        self.assertEqual(r2.__str__(), "[Rectangle] (7) 1/0 - 5/5")

    def test_update(self):
        # test positional parameters
        r1 = Rectangle(10, 10, 10, 10, 1001)
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        # --------------------------------------------------------------
        # test named parameters
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

