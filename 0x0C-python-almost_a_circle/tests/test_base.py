#!/usr/bin/python3
"""Unittest Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test Base()
    """

    def setUp(self):
        """ setup method """
        Base._clear_inits()

    def test_bad_id(self):
        """ Test non-int id passed """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base('abc')
        self.assertEqual(b2.id, 'abc')
        # with self.assertRaises(TypeError):
        #     print("TypeError")

    def test_id_increments(self):
        """ Test id incremented """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_set(self):
        """Test id is set"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    if __name__ == '__main__':
        unittest.main()
