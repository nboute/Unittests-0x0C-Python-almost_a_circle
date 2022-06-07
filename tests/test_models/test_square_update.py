#!/usr/bin/python3
"""Unittests for update() method of square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareUpdate_args(unittest.TestCase):
    """Unittest for update(*args) method of Square instance"""

    def test_args_not_specified(self):
        """Test with no specified parameters"""
        s = Square(4, 2, 3, 1)
        s.update()
        self.assertEqual("[Square] (1) 2/3 - 4", str(s))

    def test_args_one_parameter(self):
        """Test with one parameter"""
        s = Square(4, 2, 3, 1)
        s.update(5)
        self.assertEqual("[Square] (5) 2/3 - 4", str(s))

    def test_args_two_parameters(self):
        """Test with two parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6)
        self.assertEqual("[Square] (5) 2/3 - 6", str(s))

    def test_args_three_parameters(self):
        """Test with three parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7)
        self.assertEqual("[Square] (5) 7/3 - 6", str(s))

    def test_args_four_parameters(self):
        """Test with four parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        self.assertEqual("[Square] (5) 7/8 - 6", str(s))

    def test_args_multiple_call(self):
        """Test with multiple use of update() method"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_args_with_none(self):
        """Test with None"""
        s = Square(4, 2, 3, 1)
        s.update(None)
        self.assertEqual("[Square] (None) 2/3 - 4", str(s))

    def test_args_size_is_none(self):
        """Test with size is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, None)

    def test_args_x_is_none(self):
        """Test with x coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 6, None)

    def test_args_y_is_none(self):
        """Test with y coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(2, 6, 1, None)

    def test_args_size_must_be_integer(self):
        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(3600, "4")

    def test_args_size_zero(self):
        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, 0)

    def test_args_negative_size(self):
        """Test size with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, -4)

    def test_args_x_must_be_integer(self):
        """Test x coordinate with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(3600, 6, "2")

    def test_args_negative_x(self):
        """Test x coordinate with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(3600, 6, -2)

    def test_args_y_must_be_integer(self):
        """Test y coordinate with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(3600, 6, 3, "4")

    def test_args_negative_y(self):
        """Test y coordinate with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(3600, 6, 3, -4)


class TestSquareUpdate_kwargs(unittest.TestCase):
    """Unittest for update(**kwargs) method of Square instance"""

    def test_kwargs_update_id(self):
        """Test update(id=value)"""
        s = Square(4, 2, 3, 1)
        s.update(id=3600)
        self.assertEqual("[Square] (3600) 2/3 - 4", str(s))

    def test_kwargs_update_size(self):
        """Test update(size=value)"""
        s = Square(4, 2, 3, 1)
        s.update(size=8)
        self.assertEqual("[Square] (1) 2/3 - 8", str(s))

    def test_kwargs_update_x(self):
        """Test update(x=value)"""
        s = Square(4, 2, 3, 1)
        s.update(x=6)
        self.assertEqual("[Square] (1) 6/3 - 4", str(s))

    def test_kwargs_update_y(self):
        """Test update(y=value)"""
        s = Square(4, 2, 3, 1)
        s.update(y=8)
        self.assertEqual("[Square] (1) 2/8 - 4", str(s))

    def test_kwargs_update_all(self):
        """Test update(id, size, x, y)"""
        s = Square(4, 2, 3, 1)
        s.update(y=8, size=16, id=3600, x=4)
        self.assertEqual("[Square] (3600) 4/8 - 16", str(s))

    def test_kwargs_multiple_call(self):
        """Test with multiple update call"""
        s = Square(4, 2, 3, 1)
        s.update(y=8, size=16, id=3600, x=4)
        s.update(x=2, id=1, y=3, size=4)
        self.assertEqual("[Square] (1) 2/3 - 4", str(s))

    def test_kwargs_size_is_none(self):
        """Test update(size=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size=None)

    def test_kwargs_x_is_none(self):
        """Test update(x=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x=None)

    def test_kwargs_y_is_none(self):
        """Test update(y=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y=None)

    def test_kwargs_size_must_be_integer(self):
        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="4")

    def test_kwargs_size_zero(self):
        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_kwargs_negative_size(self):
        """Test size parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-4)

    def test_kwargs_x_must_be_integer(self):
        """Test x parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="2")

    def test_kwargs_negative_x(self):
        """Test x parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-2)

    def test_kwargs_y_must_be_integer(self):
        """Test y parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="3")

    def test_kwargs_negative_y(self):
        """Test y parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-3)


if __name__ == "__main__":
    unittest.main()
