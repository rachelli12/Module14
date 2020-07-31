import unittest
from anagram import anagram_class as ac

class AnagramClassTest(unittest.TestCase):
    def setUp(self):
        self.not_anagram = 'queue'
        self.is_anagram = 'racecar'
        self.word_number = 'w0rd'
        self.word_symbol = 'd$llar'
        self.capital = 'Words'
        self.lower_case = 'words'
        self.anagram = ac.Anagram(self.not_anagram)

    def tearDown(self):
        del self.anagram

    def test_constructor_symbol(self):
        """Test for symbol in word"""
        with self.assertRaises(ac.InvalidWordException):
            self.anagram = ac.Anagram(self.word_symbol)

    def test_constructor_number(self):
        """Test for number in word"""
        with self.assertRaises(ac.InvalidWordException):
            self.anagram = ac.Anagram(self.word_number)

    def test_constructor_capital(self):
        expected = 'dorsw'
        expected_anagram = ac.Anagram(self.capital)
        self.assertEqual(expected_anagram.sort_anagram(), expected)

if __name__ == '__main__':
    unittest.main()
