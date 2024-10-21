#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_id_not_None(self):
        self.assertTrue(Base(1001), self.id == 1001)
        self.assertTrue(Base(999), self.id == 999)
