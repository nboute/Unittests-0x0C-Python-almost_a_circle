"""
Unit test for the load_from_file method of the Base class
"""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareSize(unittest.TestCase):
    """ tests for load_from_file of base.py """

    def test_load_empty_file(self):
        """Tests for non existant and empty file"""
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_rectangle(self):
        """Test for loading a list of rectangles"""
        rect_a = Rectangle(2, 4)
        rect_b = Rectangle(1, 1)
        rect_c = Rectangle(6, 6)
        my_list = [rect_a, rect_b, rect_c]
        Rectangle.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")

    def test_load_square(self):
        """Test for loading a list of squares"""
        rect_a = Square(2)
        rect_b = Square(1)
        rect_c = Square(6)
        my_list = [rect_a, rect_b, rect_c]
        Square.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")

    def test_extra_args(self):
        """Test calling the function with an additional argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file("Hello")
