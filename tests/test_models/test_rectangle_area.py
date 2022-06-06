#!/usr/bin/python3
"""
Unit test for the class Base and Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestArea(unittest.TestCase):
    """ test area for class rectangle.py """
    def test_area_rectangle1(self):
        """ test with 2 integers """
        a = Rectangle(3, 5)
        self.assertEqual(a.area(), 15)

    def test_area_rectangle2(self):
        """ test with float for width and int for height"""
        with self.assertRaises(TypeError):
            a = Rectangle(0.3, 5)
            a.area()

    def test_area_rectangle3(self):
        """ test with int for width and float for heigt """
        with self.assertRaises(TypeError):
            a = Rectangle(3, 0.5)
            a.area()

    def test_area_rectangle4(self):
        """ test with 0 for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(0, 5)
            a.area()

    def test_area_rectangle5(self):
        """ test with int for widht and 0 for height """
        with self.assertRaises(ValueError):
            a = Rectangle(3, 0)
            a.area()

    def test_area_rectangle6(self):
        """ test for negative for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, 5)
            a.area()

    def test_area_rectangle7(self):
        """ test with negative for width & height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, -5)
            a.area()

    def test_area_rectangle8(self):
        """ test with 1 arg """
        with self.assertRaises(TypeError):
            a = Rectangle(3)
            a.area()

    def test_area_rectangle9(self):
        """ test without arg """
        with self.assertRaises(TypeError):
            a = Rectangle()
            a.area()

    def test_area_rectangle10(self):
        """ test with arg None """
        with self.assertRaises(TypeError):
            a = Rectangle(None)
            a.area()

    def test_area_rectangle11(self):
        """ test with function for width and int for height """
        with self.assertRaises(UnboundLocalError):
            a = Rectangle(a.area(), 6)
            a.area()

    def test_area_rectangle12(self):
        """ test with strings """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", "World")
            a.area()

    def test_area_rectangle13(self):
        """ test with tuples """
        with self.assertRaises(TypeError):
            a = Rectangle((1, 2, 3), (1, 2, 3))
            a.area()

    def test_area_rectangle14(self):
        """ test with lists """
        with self.assertRaises(TypeError):
            a = Rectangle([1, 2, 3], [1, 2, 3])
            a.area()

    def test_area_rectangle15(self):
        """ test with dictionaries """
        with self.assertRaises(TypeError):
            a = Rectangle({1, 2, 3}, {1, 2, 3})
            a.area()

    def test_area_rectangle16(self):
        """ test with float("inf") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("inf"), 3)
            a.area()

    def test_area_rectangle17(self):
        """ test float("Nan") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("NaN"), 5)
            a.area()

    def test_area_rectangle18(self):
        """ test with None for args """
        with self.assertRaises(TypeError):
            a = Rectangle(None, None)
            a.area()

    def test_area_rectangle19(self):
        """ test with string for width int for height """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", 5)
            a.area()

    def test_area_rectangle20(self):
        """ test with int for width string for height """
        with self.assertRaises(TypeError):
            a = Rectangle(3, "World")
            a.area()

    def test_area_rectangle21(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!")
            a.area()

    def test_area_rectangle22(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle.area()


if __name__ == "__main__":
    unittest.main()
