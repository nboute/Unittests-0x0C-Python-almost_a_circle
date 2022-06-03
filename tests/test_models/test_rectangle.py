#!/usr/bin/python3
"""
    Unittest for Rectangle
"""

from distutils.util import run_2to3
import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
        tests for Rectangle
    """
    def test_weight_is_integer(self):
        """
            test weight is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 10)
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)
        with self.assertRaises(TypeError):
            Rectangle(2.3, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 2)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2)
        with self.assertRaises(TypeError):
            Rectangle("abc", 2)
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 2)

    def test_height_is_integer(self):
        """
            test height is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -4)
        with self.assertRaises(TypeError):
            Rectangle(2, 5.3)
        with self.assertRaises(TypeError):
            Rectangle(2, None)
        with self.assertRaises(TypeError):
            Rectangle(2, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(10,"hello" ,2 , 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, {1, 2}, 0, 0, 12)

    def test_x_is_integer(self):
        """
            test x is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 0, 12)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3.5, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('inf'), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "hello", 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {1 , 2}, 0, 12)

    def test_y_is_integer(self):
        """
            test y is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 2, 12)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -2, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 2.6, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, None, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, float('inf'), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, (1, 2, 3), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "hello", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {1 , 2}, 12)

    def test_area(self):
        """
            test the calculation of the area
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 3, 3, 2, 12)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 30)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2, 0, 0, 12)
            r3.area()
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 3, 3, 2, 12)
            r4.area()


if __name__ == '__main__':
    unittest.main()
