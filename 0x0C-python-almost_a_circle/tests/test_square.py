#!/usr/bin/python3
"""Unittest Square"""
import unittest
from models.square import Square
from models.base import Base

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::


class TestSquare(unittest.TestCase):

    """ Test Square(Rectangle)"""

    def setUp(self):
        # super(Base, self).setUp()
        # _Square._clear_inits()
        Base._clear_inits()

    def test_bad_id(self):
        """ Test non-int id passed """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)
        # with self.assertRaises(TypeError):
        #     r2.id

    def test_id_increments(self):
        """ Test id incremented """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Square(12, 1)
        self.assertEqual(r3.id, 3)

        r4 = Square(10, 2, 0, 1)
        self.assertEqual(r4.id, 4)

    def test_id_set(self):
        """ Test id set """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)

        r2 = Square(12, 2)
        self.assertEqual(r2.id, 2)

        r3 = Square(10, 2, 0, 1, 13)
        self.assertEqual(r3.id, 13)

        """ otherwise, increment __nb_objects and assign the new value
         to the public instance attribute id """

    def test_width(self):
        # r4 = Square(10, 3)
        self.assertEqual(Square(10, 3).width, 10)

    def test_height(self):
        r1 = Square(10, 3)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_nodimensions(self):
        with self.assertRaises(ValueError) as jfk:
            Square(0, None, 5, 4)
        self.assertEqual(str(jfk.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Square(3, None, 5, 3)

        r1 = Square(1, 2, 5, 4)
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 3)

    def test_x(self):
        self.assertEqual(Square(10, 3).width, 10)

    def test_y(self):
        self.assertEqual(Square(10, 3).width, 10)

    def test_width(self):
        self.assertEqual(Square(10, 3).width, 10)

    def test_area(self):
        r1 = Square(1, 2, 5, 4)
        self.assertEqual(r1.area(), 2)

        r2 = Square(5, 2, 5, 4)
        self.assertEqual(r2.area(), 10)

        r1 = Square(2, 5, 5, 4)
        self.assertEqual(r1.area(), 10)

    # def test_output(self):
    #     from contextlib import redirect_stdout
    #     from io import StringIO
    #     f = StringIO()
    #     print(f)
    #     with redirect_stdout(f):
    #         # help(pow)
    #         r1 = Square(2, 2, 3, 5)
    #         r1.display()
    #     s = f.getvalue()
    #     self.assertEqual(s, r1)

        # ATTEMPT #2
        # import sys
        # from contextlib import contextmanager
        # from io import StringIO

        # @contextmanager
        # def captured_output():
        #     new_out, new_err = StringIO(), StringIO()
        #     old_out, old_err = sys.stdout, sys.stderr
        #     try:
        #         sys.stdout, sys.stderr = new_out, new_err
        #         yield sys.stdout, sys.stderr
        #     finally:
        #         sys.stdout, sys.stderr = old_out, old_err

        # with captured_output() as (out, err):
        #     r1 = Square(2, 2, 2, 2)
        #     r1.display()

        # lines = out.getvalue().splitlines()
        # self.assertIn('xxx', lines)

if __name__ == '__main__':
    unittest.main()
