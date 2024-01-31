#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    A unittest module to test the max_integer function.

    Methods:
    - setUpClass(cls): Class-level setup method to initialize common resources.
    - test_max_integer(self):Test case for max_integer with a list of integers.
    - test_max_integer2(self): Test case for max_integer with another list of
        integers.
    - test_max_integer3(self): Test case for max_integer with a list of
        negative integers.
    - test_max_integer4(self): Test case for max_integer with another list of
        negative integers.
    - test_max_integer_float(self): Test case for max_integer with a list of
        integers and floats.
    - test_max_integer_float2(self): Test case for max_integer with a list of
        integers and negative floats.
    - test_max_only_float(self): Test case for max_integer with a list of only
        positive floats.
    - test_max_only_float2(self): Test case for max_integer with a list of only
        negative floats.
    - test_max_int1(self): Test case for max_integer with a list containing a
        single positive integer.
    - test_max_int2(self): Test case for max_integer with a list containing a
        single negative integer.
    - test_max_flo1(self): Test case for max_integer with a list containing a
        single positive float.
    - test_max_flo2(self): Test case for max_integer with a list containing a
        single negative float.
    - test_max_string(self): Test case for max_integer with a list of strings.
    - test_max_str1(self): Test case for max_integer with a list containing a
        single string.
    - test_max_str2(self): Test case for max_integer with a string instead
        of a list.
    - test_empty(self): Test case for max_integer with an empty list.
    - test_empty2(self): Test case for max_integer with a list containing an
        empty string.
    - test_empty3(self): Test case for max_integer with an empty string
        instead of a list.
    """

    @classmethod
    def setUpClass(cls):
        """
        Class-level setup method to initialize common resources.
        """
        cls.lists_integers = [1, 2, 3, 4]
        cls.lists_integers2 = [4, 2, 5, 4]
        cls.lists_integers3 = [-5, 2, 3, -4]
        cls.lists_integers4 = [-5, -2, -3, -4]
        cls.lists_int_floats = [1, 7.3, 4.5, 2]
        cls.lists_int_floats2 = [1, -7.3, 4.5, -2]
        cls.lists_only_floats = [9.8, 7.3, 4.5, 2.0]
        cls.lists_only_floats2 = [-9.8, -7.3, -4.5, -2.0]
        cls.lists_int1 = [2]
        cls.lists_int2 = [-2]
        cls.lists_flo1 = [2.7]
        cls.lists_flo2 = [-2.7]
        cls.lists_strings = ["Anas", "Mouak", "fff", "ggg"]
        cls.lists_string1 = ["Anas"]
        cls.lists_string2 = "Anas"
        cls.lists_empty = []
        cls.lists_empty2 = [""]
        cls.lists_empty3 = ""

    def test_max_integer(self):
        """
        Test case for max_integer with a list of integers.
        """
        self.assertEqual(max_integer(self.lists_integers), 4)

    def test_max_integer2(self):
        """
        Test case for max_integer with another list of integers.
        """
        self.assertEqual(max_integer(self.lists_integers2), 5)

    def test_max_integer3(self):
        """
        Test case for max_integer with a list of negative integers.
        """
        self.assertEqual(max_integer(self.lists_integers3), 3)

    def test_max_integer4(self):
        """
        Test case for max_integer with another list of negative integers.
        """
        self.assertEqual(max_integer(self.lists_integers4), -2)

    def test_max_integer_float(self):
        """
        Test case for max_integer with a list of integers and floats.
        """
        self.assertEqual(max_integer(self.lists_int_floats), 7.3)

    def test_max_integer_float2(self):
        """
        Test case for max_integer with a list of integers and negative floats.
        """
        self.assertEqual(max_integer(self.lists_int_floats2), 4.5)

    def test_max_only_float(self):
        """
        Test case for max_integer with a list of only positive floats.
        """
        self.assertEqual(max_integer(self.lists_only_floats), 9.8)

    def test_max_only_float2(self):
        """
        Test case for max_integer with a list of only negative floats.
        """
        self.assertEqual(max_integer(self.lists_only_floats2), -2.0)

    def test_max_int1(self):
        """
        Test case for max_integer with a list containing a single positive
        integer.
        """
        self.assertEqual(max_integer(self.lists_int1), 2)

    def test_max_int2(self):
        """
        Test case for max_integer with a list containing a single negative
        integer.
        """
        self.assertEqual(max_integer(self.lists_int2), -2)

    def test_max_flo1(self):
        """
        Test case for max_integer with a list containing a single positive
        float.
        """
        self.assertEqual(max_integer(self.lists_flo1), 2.7)

    def test_max_flo2(self):
        """
        Test case for max_integer with a list containing a single negative
        float.
        """
        self.assertEqual(max_integer(self.lists_flo2), -2.7)

    def test_max_string(self):
        """
        Test case for max_integer with a list of strings.
        """
        self.assertEqual(max_integer(self.lists_strings), "ggg")

    def test_max_str1(self):
        """
        Test case for max_integer with a list containing a single string.
        """
        self.assertEqual(max_integer(self.lists_string1), "Anas")

    def test_max_str2(self):
        """
        Test case for max_integer with a string instead of a list.
        """
        self.assertEqual(max_integer(self.lists_string2), "s")

    def test_empty(self):
        """
        Test case for max_integer with an empty list.
        """
        self.assertEqual(max_integer(self.lists_empty), None)

    def test_empty2(self):
        """
        Test case for max_integer with a list containing an empty string.
        """
        self.assertEqual(max_integer(self.lists_empty2), "")

    def test_empty3(self):
        """
        Test case for max_integer with an empty string instead of a list.
        """
        self.assertEqual(max_integer(self.lists_empty3), None)


if __name__ == '__main__':
    unittest.main()
