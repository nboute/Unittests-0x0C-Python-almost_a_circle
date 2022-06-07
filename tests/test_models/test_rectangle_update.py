#!/usr/bin/python3
"""
Unit test for the class Base and Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestUpdate(unittest.TestCase):
    """ test update for class rectangle.py """
    def test_update1(self):
        """ test without args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update()
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10', str(a))

    def test_update2(self):
        """ test with 1 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(a))
    
    def test_update3(self):
        """ test with 2 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1)
        self.assertEqual("[Rectangle] (89) 10/10 - 1/10", str(a))

    def test_update4(self):
        """ test with 3 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 1/2", str(a))

    def test_update5(self):
        """ test with 4 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3)
        self.assertEqual("[Rectangle] (89) 3/10 - 1/2", str(a))

    def test_update6(self):
        """ test with 5 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(a))

    def test_update7(self):
        """ test with id None """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None)
        self.assertEqual("[Rectangle] (None) 10/10 - 10/10", str(a))

    def test_update8(self):
        """ test with id None and args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None, 1, 2, 3)
        self.assertEqual("[Rectangle] (None) 3/10 - 1/2", str(a))

    def test_update9(self):
        """ test with twice update """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3, 4)
        a.update(5, 6, 7, 8, 9)
        self.assertEqual("[Rectangle] (5) 8/9 - 6/7", str(a))

    def test_update10(self):
        """ test with strings for width """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!")

    def test_update11(self):
        """ test with 0 for width"""
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(89, 0)

    def test_update12(self):
        """ test with negative for width """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(89, -1)

    def test_update13(self):
        """ test update with string for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.update(89, 1, "Hello!")

    def test_update14(self):
        """ test with 0 for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.update(89, 1, 0)

    def test_update15(self):
        """ test with negative for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.update(89, 1, -2)

    def test_update16(self):
        """ test with string for x """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(89, 1, 2, "Hello!")

    def test_update17(self):
        """ test with negative for y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            a.update(89, 1, 2, 3, -4)

    def test_update18(self):
        """ test with strings for width and height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", "World")

    def test_update19(self):
        """ test with strings for width and x """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", 1, "World")

    def test_update20(self):
        """ test with strings for width and y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", 1, 2, "World")

    def test_update21(self):
        """ test with strings for x and y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.update(89, 1, "Hello!", "World")

    def test_update22(self):
        """ test with strings height and y """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "Hello!", 1, "World")

    def test_update23(self):
        """ test with strings for x and y """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "Hello!", "World")

    def test_update24(self):
        """ test with id 0 """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(0)
        correct = f"[Rectangle] (0) 10/10 - 10/10"
        self.assertEqual(correct, str(a))

    def test_update25(self):
        """ test with id None """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(-1)
        correct = f"[Rectangle] (-1) 10/10 - 10/10"
        self.assertEqual(correct, str(a))

    def test_update26(self):
        """ test with 4 attributes and without args"""
        a = Rectangle(10, 10, 10, 10)
        a.update()
        self.assertEqual('[Rectangle] (1) 10/10 - 10/10', str(a))

    def test_update27(self):
        """ test with args width is negative"""
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(width=-1, x=2, id=98)

    def test_update28(self):
        """ test with 3 attributes """
        a = Rectangle(10, 10, 10)
        a.update(98)
        self.assertEqual('[Rectangle] (98) 10/0 - 10/10', str(a))

    def test_update29(self):
        """ test with 3 attributes and without args """
        a = Rectangle(10, 10)
        a.update(98)
        self.assertEqual('[Rectangle] (98) 0/0 - 10/10', str(a))

    def test_update30(self):
        """ test with 3 attributes and without args """
        a = Rectangle(10, 10, 10, 10)
        a.update(width=1, x=2, id=98)
        self.assertEqual('[Rectangle] (98) 2/10 - 1/10', str(a))

    def test_update31(self):
        """ test with args x is string """
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(width=1, x="Hello!", id=98)

    def test_update32(self):
        """ test with args x is string """
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(width=0, x=2, id=98)


if __name__ == "__main__":
    unittest.main()