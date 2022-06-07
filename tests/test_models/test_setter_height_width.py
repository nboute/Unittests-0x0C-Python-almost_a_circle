"""
Unit test for setter/getter of height and width
"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestRectangle_setter_getter(unittest.TestCase):
    """test getter setter of the rectangle height and width"""
    def test_height_getter(self):
        """test for the getter of the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(3, rect.height)

    def test_height_setter(self):
        """test to set an int to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def test_height_setter_negative(self):
        """test to set a negative int to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.height = -12

    def test_height_setter_float(self):
        """test to set a float to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = 1.2

    def test_height_setter_string(self):
        """test to set a string to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = "ok"

    def test_height_setter_list(self):
        """test to set a list to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = [12]

    def test_height_setter_tuple(self):
        """test to set a tuple to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = (1, 2)

    def test_height_setter_dict(self):
        """test to set a dictonary to the height"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = {12}
            
    def test_width_getter(self):
        """test for the getter of the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(2, rect.width)

    def test_width_setter(self):
        """test to set an int to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.width = 12
        self.assertEqual(12, rect.width)

    def test_width_setter_negative(self):
        """test to set a negative int to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
                rect.width = -12

    def test_width_setter_float(self):
        """test to set a float to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
                rect.width = 1.2

    def test_width_setter_string(self):
        """test to set a string to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
                rect.width = "ok"

    def test_width_setter_list(self):
        """test to set a list to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
                rect.width = [12]

    def test_width_setter_tuple(self):
        """test to set a tuple to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
                rect.width = (1, 2)

    def test_width_setter_dict(self):
        """test to set a dictionary to the width"""
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
                rect.width = {12}

if __name__ == '__main__':
    unittest.main()
