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
        """test if value is neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2, -2, -0, -12)

    def test_value_is_x_heigt_not_neg(self):
        """test if x and x is not neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, -2, -0, -12)

    def test_value_is_x_neg(self):
        """test if x neg
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 1, -1, 12)

    def test_value_is_not_tuple(self):
        """test W and H with tuples
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, (1, -10), 12)

    def test_y_is_not_tuple(self):
        """test X and Y with tuples
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, -10, -2, (1, 10) - 12)

    def test_value_is_not_list(self):
        """test W and H with list
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [1, -10], 12)

    def test_value_is_not_dict(self):
        """test W with dict
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, 2, {'lolo': -10}, 12)

    def test_value_is_not_empty(self):
        """test empy instance
        """
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_display_None(self):
        """test with None
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)

    def test_x_setter(self):
        """Test x setter"""
        r = Rectangle(5, 7, 0, 0, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(5, 7, 30, 30, 10)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_x_setter_neg(self):
        """Test x setter neg"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 7, 30, 30, 1)
            r.x = -10

    def test_y_setter_neg(self):
        """Test y setter negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 7, 10, 30, 1)
            r.y = -10

    def test_x_setter_string(self):
        """Test x setter string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = "lolo"

    def test_y_setter_string(self):
        """Test y setter string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.y = "lolo"

    def test_x_setter_empty(self):
        """Test x empty"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = None

    def test_y_setter_empty(self):
        """Test y empty"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.y = None

    def test_x_setter_tuple(self):
        """Test x tuple"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 0, 0, 1)
            r.x = (1, 2)

    def test_y_setter_tuple(self):
        """Test y tuple"""
        r = Rectangle(1, 7, 0, 0, 1)
        with self.assertRaises(TypeError):
            r.y = (1, 2)

    def test_x_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(4, rect.x)

    def test_y_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(5, rect.y)


if __name__ == '__main__':
    unittest.main()
