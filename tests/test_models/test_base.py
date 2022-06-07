#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
from models import base
Base = base.Base



class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 6.3)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])


if __name__ == '__main__':
    unittest.main()
