#!/usr/bin/python3
"""unittest module"""
import unittest
from unittest.mock import patch
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class testing the to_dictionary method and __str__ of Rectangle"""
    def test_to_dictionary(self):
        """test the to_dictionary method"""
        Base._Base__nb_objects = 0
        a = Rectangle(6, 2)
        output = {'id': 1, 'width': 6, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(1, 3, 5)
        output = {'id': 2, 'width': 1, 'height': 3, 'x': 5, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(4, 4, 1, 6)
        output = {'id': 3, 'width': 4, 'height': 4, 'x': 1, 'y': 6}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(2, 7, 4, 2, 18)
        output = {'id': 18, 'width': 2, 'height': 7, 'x': 4, 'y': 2}
        self.assertDictEqual(a.to_dictionary(), output)

    def test_str(self):
        """test the output of the instance when printed"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(4, 8))
        assert fake_stdout.getvalue() == '[Rectangle] (1) 0/0 - 4/8\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(1, 3, 5, 7, 12))
        assert fake_stdout.getvalue() == '[Rectangle] (12) 5/7 - 1/3\n'

    def test_exception(self):
        """test with exception"""
        a = Rectangle(1, 2, 3, 4, 6)
        self.assertRaises(TypeError, a.to_dictionary, 0)
        a = Rectangle(1, 2)
        self.assertRaises(TypeError, a.to_dictionary, None)

    if __name__ == "__main__":
        unittest.main()
