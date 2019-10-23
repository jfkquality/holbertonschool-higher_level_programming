#!/usr/bin/python3
"""Unittest Square"""
import unittest
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):

    """
    Test Rectangle(Base)
    if id is not None, assign the public instance attribute id with this
    argument's value - you can assume id is an integer
    and you don’t need to test the type of it
    """

    def setUp(self):
        """Test setup"""
        Base._clear_inits()

    def test_bad_id(self):
        """ Test non-int id passed """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)

    def test_id_increments(self):
        """ Test id incremented """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Square(12, 1)
        self.assertEqual(r3.id, 3)

        r4 = Square(10, 2, 0, 1)
        self.assertEqual(r4.id, 1)

    def test_id_set(self):
        """ Test id set """
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.x, 2)

        r2 = Square(12, 2)
        self.assertEqual(r2.id, 2)

        r3 = Square(10, 2, 1, 13)
        self.assertEqual(r3.id, 13)

    def test_size(self):
        """Test width"""
        # r4 = Square(10, 3)
        self.assertEqual(Square(10, 3).size, 10)

    def test_nodimensions(self):
        """Test no dimensions"""
        with self.assertRaises(ValueError) as jfk:
            Square(0, None, 5, 4)
        self.assertEqual(str(jfk.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Square(3, None, 5, 3)

    def test_x(self):
        """Test x coord"""
        self.assertEqual(Square(10, 3).size, 10)

    def test_y(self):
        """Test y coord"""
        self.assertEqual(Square(10, 3).size, 10)

    def test_width(self):
        """Test width coord"""
        self.assertEqual(Square(10, 3).size, 10)

    def test_area(self):
        """Test area coord"""
        r1 = Square(1, 2, 5, 4)
        self.assertEqual(r1.area(), 1)

        r2 = Square(5, 2, 5, 4)
        self.assertEqual(r2.area(), 25)

        r1 = Square(2, 5, 5, 4)
        self.assertEqual(r1.area(), 4)

    # def test_output(self):
    #    """Test x coord"""
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

    def test_x2y2_print(self):
        """ Tests if x2y2 rectangle prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(2, 3, 2, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '\n\n   ##\n   ##\n')


    def test_args_print(self):
        """ Test if args update attributes, prints
        """
        from io import StringIO
        import io
        import contextlib

        r1 = Square(10, 10, 10, 10)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (10) 10/10 - 10\n')

        r1.update(89)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 10/10 - 10\n')

        r1.update(89, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 10/10 - 2\n')

        r1.update(89, 2, 3)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/10 - 2\n')

        r1.update(89, 2, 3, 4)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/4 - 2\n')

        r1.update(89, 2, 4, 5)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 4/5 - 2\n')

    def test_xargs_print(self):
        """ Test if xargs updates, prints
        """
        from io import StringIO
        import io
        import contextlib

        r1 = Square(10, 10, 10, 10)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (10) 10/10 - 10\n')

        r1.update(size=1, x=2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (10) 2/10 - 1\n')

        r1.update(y=1, size=2, x=3, id=89)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 3/1 - 2\n')

        r1.update(x=1, y=3, size=4)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 1/3 - 4\n')


    if __name__ == '__main__':
        unittest.main()
