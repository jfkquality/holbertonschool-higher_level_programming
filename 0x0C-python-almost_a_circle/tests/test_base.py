"""Unittest Base"""
import unittest
from models.base import Base

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::

# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::


class TestBase(unittest.TestCase):

    """
    Test Base()
    if id is not None, assign the public instance attribute id with this
    argument's value - you can assume id is an integer
    and you don’t need to test the type of it
    """

    def setUp(self):
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
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 2)

        """ otherwise, increment __nb_objects and assign the new value
         to the public instance attribute id """

        if __name__ == '__main__':
            unittest.main()

if __name__ == '__main__':
    unittest.main()
