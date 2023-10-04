#!/usr/bin/python3
"""Unit tests for the max_integer() function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class for the max_integer() function"""
    
    def test_module_docstring(self):
        """Test the module docstring"""
        module_docstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_docstring) > 1)

    def test_function_docstring(self):
        """Test the function docstring"""
        function_docstring = max_integer.__doc__
        self.assertTrue(len(function_docstring) > 1)

    def test_empty_list(self):
        """Test an empty list"""
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_no_args(self):
        """Test no arguments passed to the function"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with only one number"""
        one_element_list = [1]
        self.assertEqual(max_integer(one_element_list), 1)

    def test_positive_end(self):
        """Test a list with all positive numbers, max at the end"""
        positive_end_list = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_end_list), 50)

    def test_positive_middle(self):
        """Test a list with all positive numbers, max in the middle"""
        positive_middle_list = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(positive_middle_list), 360)

    def test_positive_beginning(self):
        """Test a list with all positive numbers, max at the beginning"""
        positive_beginning_list = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(positive_beginning_list), 200)

    def test_one_negative(self):
        """Test a list with one negative number"""
        one_negative_list = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(one_negative_list), 200)

    def test_all_negative(self):
        """Test a list with all negative numbers"""
        all_negative_list = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(all_negative_list), -1)

    def test_none_as_argument(self):
        """Test passing None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_argument(self):
        """Test a non-int type in the list"""
        non_int_list = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(non_int_list)

if __name__ == "__main__":
    unittest.main()

