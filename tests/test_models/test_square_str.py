#!/usr/bin/python3
"""
Add unittest for the Square class
"""
import unittest
from models.square import Square
from models.base import Base


class Test_str_square(unittest.TestCase):
    """tests for the str of square"""
    Base._Base__nb_objects = 0

    def test_str(self):
        """test normal use of str function"""
        s1 = Square(2, 1, 3, 6)
        self.assertEqual("[Square] (6) 1/3 - 2", str(s1))

    def test_str1(self):
        """test less informations"""
        s2 = Square(2, 1)
        self.assertEqual("[Square] (24) 1/0 - 2", str(s2))
        s3 = Square(3, 1, 6)
        self.assertEqual("[Square] (25) 1/6 - 3", str(s3))
        s4 = Square(3)
        self.assertEqual("[Square] (26) 0/0 - 3", str(s4))
        with self.assertRaises(TypeError):
            Square()

    def test_str2(self):
        """test wrong informations"""
        with self.assertRaises(ValueError):
            Square(-2)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(TypeError):
            Square(3.2)
        with self.assertRaises(TypeError):
            Square({1, 2})
        with self.assertRaises(TypeError):
            Square([1, 34])
        with self.assertRaises(TypeError):
            Square(float('inf'))


if __name__ == '__main__':
    unittest.main()
