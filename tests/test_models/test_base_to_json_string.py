#!/usr/bin/python3
"""Unittests for to_json_string(list_dictionaries)"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestToJsonString(unittest.TestCase):
    """Unittest for to_json_string"""
    def test_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))

    def test_rectangle_instance(self):
        """Test rectangle instance with len()"""
        r1 = Rectangle(10, 7, 6, 4, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(len(json_dictionary) == 53)

    def test_more_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_rectangle_instances(self):
        """Test rectangle instances with len()"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 106)

    def test_square_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(str, type(json_dictionary))

    def test_square_instance(self):
        """Test square instance with len()"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertTrue(len(json_dictionary) == 37)

    def test_more_squares_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_square_instances(self):
        """Test square instances with len()"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 77)

    def test_empty(self):
        """Test with empty value"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """Test with None"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_parameters(self):
        """Test if no parameter (list_dicitonaries)"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_parameters(self):
        """Test if more undefined parameters"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3600)


if __name__ == "__main__":
    unittest.main()
