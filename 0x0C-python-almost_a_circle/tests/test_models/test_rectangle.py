#!/usr/bin/python3
"""

A unit test for rectangle class
# Run python3 -m unittest discover tests
# Run python3 -m unittest tests/test_models/test_base.py
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
        Rec.x = 3.1
        Rec.y = 4.2
        self.assertEqual(Rec.width, 3000)
        self.assertEqual(Rec.height, 4000)
        self.assertEqual(Rec.x, 3.1)
        self.assertEqual(Rec.y, 4.2)
        with self.assertRaises(ValueError):
            Rec.width = -200