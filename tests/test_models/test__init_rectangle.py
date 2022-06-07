#!/usr/bin/python3
"""
    Unittest for Rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
        tests for Rectangle
    """

    def test_rectangle_is_instance_of_base(self):
        """Test if the Rect is an instance of base
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r1, Base)

    def test_value_is_int(self):
        """Test if the value for init is an int
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("f", "f", "f", "f", "f")

    def test_value_is_negativ(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2, -2, -0, -12)

    def test_value_is_width_heigt_not_neg(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, -2, -0, -12)

    def test_value_is_x_y_not_neg(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, -1, -1, 12)

    def test_value_is_not_tuple(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle((1, -10), -2, -2, -0, -12)

    def test_value_is_not_list(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle([1, -10], -2, -2, -0, -12)

    def test_value_is_not_dict(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle({'lolo': -10}, -2, -2, -0, -12)

    def test_value_is_not_empty(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_display_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)


if __name__ == '__main__':
    unittest.main()
