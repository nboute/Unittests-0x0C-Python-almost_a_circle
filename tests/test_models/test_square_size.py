"""
Unit test for the size setter/getter methods of the Square class
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestSquareSize(unittest.TestCase):
    """ tests for size setter/getter of square.py """

    def test_square_size1(self):
        """ test without args """
        with self.assertRaises(TypeError):
            Square.size()

    def test_square_size2(self):
        """test getter"""
        my_square = Square(2)
        self.assertEqual(my_square.size, 2)

    def test_square_size3(self):
        """test setter"""
        my_square = Square(2)
        my_square.size = 7
        self.assertEqual(my_square.size, 7)

    def test_square_size4(self):
        """test setter with 0"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = 0

    def test_square_size5(self):
        """test setter with negative value"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = -5

    def test_square_size6(self):
        """test setter with wrong type: float"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = 4.5

    def test_square_size7(self):
        """test setter with wrong type: string"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = "School"

    def test_square_size8(self):
        """test setter with wrong type: list"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = [4]

    def test_square_size9(self):
        """test setter with wrong type: tuple"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = (4, )

    def test_square_size10(self):
        """test setter with wrong type: dictionary"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = {4}
