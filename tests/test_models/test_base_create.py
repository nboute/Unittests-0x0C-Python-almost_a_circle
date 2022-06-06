#!/usr/bin/python3
"""
    Unittest for the create function of the Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base_Create(unittest.TestCase):
    """class test of the create base function"""

    def test_rectangle_create(self):
        """test rectangle creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_create(self):
        """test square creation"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)


if __name__ == '__main__':
    unittest.main()
