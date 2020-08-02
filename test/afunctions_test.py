"""
Program: afunctions_test.py
Author: Rachel Li
Last date modified: 02/08/2020

This program tests constructors of anagram_functions
"""
import unittest
from anagram.anagram_functions import *

class AnagramClassTest(unittest.TestCase):
    def setUp(self):
        self.not_anagram = 'queue'
        self.is_anagram = 'racecar'
        self.word_number = 'w0rd'
        self.word_symbol = 'd$llar'
        self.capital = 'Words'
        self.lower_case = 'words'
        self.anagram = Anagram_Functions(self.not_anagram)

    def tearDown(self):
        del self.anagram

    def test_constructor_symbol(self):
        """Test for symbol in word"""
        with self.assertRaises(InvalidWordException):
            self.anagram = Anagram_Functions(self.word_symbol)

    def test_constructor_number(self):
        """Test for number in word"""
        with self.assertRaises(InvalidWordException):
            self.anagram = Anagram_Functions(self.word_number)

    def test_constructor_capital(self):
        expected = 'dorsw'
        expected_anagram = (self.capital)
        self.assertEqual(expected_anagram.main(), expected)

if __name__ == '__main__':
    unittest.main()
