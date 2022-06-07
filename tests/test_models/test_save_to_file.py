#!/usr/bin/python3
"""
Add unit test for the class Base
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_one_rectangle(self):
        """test for one rectangle"""
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_two_rectangles(self):
        """test for two rectangles"""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_one_square(self):
        """test for one square"""
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_two_squares(self):
        """test for two squares"""
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_overwrite(self):
        """test for overwrite"""
        square = Square(8, 5, 9, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_empty_list(self):
        """test for an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_no_args(self):
        """test for no argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_two_arg(self):
        """test for two arguments"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

if __name__ == "__main__":
    unittest.main()
