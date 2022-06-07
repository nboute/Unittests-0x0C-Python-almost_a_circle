#!/usr/bin/python3
"""
    Unittest for the init function of the Base class
"""

import unittest
from models.base import Base


class Test_Base_Init(unittest.TestCase):
    """class test of the init base function"""

    def test_id_int(self):
        """Test integer id"""
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_incrementation(self):
        """Test id incrementation"""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        """Test non integer id"""
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Betty"})
        self.assertEqual(b.id, {"id": 7, "name": "Betty"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        """Test error"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)


if __name__ == '__main__':
    unittest.main()
