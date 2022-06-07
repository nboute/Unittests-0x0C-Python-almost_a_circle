#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
import pycodestyle
from models import base
from models import rectangle
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class TestBase(unittest.TestCase):
    """
        test for comments for base rectangle and square files
    """
    def test_conformance_base(self):
        """
            Test that we conform to PEP-8 for Base
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_rectangle(self):
        """
            Test that we conform to PEP-8 for Rectangle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_conformance_square(self):
        """
            Test that we conform to PEP-8 for Square
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
