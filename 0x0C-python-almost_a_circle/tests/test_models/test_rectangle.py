#!/usr/bin/python3
"""Unittest Rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::


class TestRectangle(unittest.TestCase):

    """
    Test Rectangle(Base)
    if id is not None, assign the public instance attribute id with this
    argument's value - you can assume id is an integer
    and you don’t need to test the type of it
    """

    def setUp(self):
        """Test setup"""
        # super(Base, self).setUp()
        # _Rectangle._clear_inits()
        Base._clear_inits()

    def test_bad_id(self):
        """ Test non-int id passed """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        # with self.assertRaises(TypeError):
        #     r2.id

    def test_id_increments(self):
        """ Test id incremented """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(12, 1)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(10, 2, 0, 1)
        self.assertEqual(r4.id, 4)

    def test_id_set(self):
        """ Test id set """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(12, 2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 1, 13)
        self.assertEqual(r3.id, 13)

    def test_width(self):
        """Test width"""
        # r4 = Rectangle(10, 3)
        self.assertEqual(Rectangle(10, 3).width, 10)

    def test_height(self):
        """Test height"""
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_nodimensions(self):
        """Test no dimensions"""
        with self.assertRaises(ValueError) as jfk:
            Rectangle(0, None, 5, 4)
        self.assertEqual(str(jfk.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Rectangle(3, None, 5, 3)

        r1 = Rectangle(1, 2, 5, 4)
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 3)

    def test_x(self):
        """Test x coord"""
        self.assertEqual(Rectangle(10, 3).width, 10)

    def test_y(self):
        """Test y coord"""
        self.assertEqual(Rectangle(10, 3).width, 10)

    def test_width(self):
        """Test width coord"""
        self.assertEqual(Rectangle(10, 3).width, 10)

    def test_area(self):
        """Test area coord"""
        r1 = Rectangle(1, 2, 5, 4)
        self.assertEqual(r1.area(), 2)

        r2 = Rectangle(5, 2, 5, 4)
        self.assertEqual(r2.area(), 10)

        r1 = Rectangle(2, 5, 5, 4)
        self.assertEqual(r1.area(), 10)

    # def test_output(self):
    #    """Test x coord"""
    #     from contextlib import redirect_stdout
    #     from io import StringIO
    #     f = StringIO()
    #     print(f)
    #     with redirect_stdout(f):
    #         # help(pow)
    #         r1 = Rectangle(2, 2, 3, 5)
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
    #     r1 = Rectangle(2, 2, 2, 2)
    #     r1.display()

    # lines = out.getvalue().splitlines()
    # self.assertIn('xxx', lines)

    if __name__ == '__main__':
        unittest.main()
