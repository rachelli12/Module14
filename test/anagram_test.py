import unittest
from anagram import anagram_class as ac
from anagram.anagram_class import Anagram

class AnagramClassTest(unittest.TestCase):
    def setUp(self):
        self.not_anagram = 'queue'
        self.is_anagram = 'racecar'
        self.word_number = 'w0rd'
        self.word_symbol = 'd$llar'
        self.capital = 'Words'
        self.lower_case = 'words'
        self.anagram = Anagram(self.not_anagram)

    def tearDown(self):
        del self.anagram

    def test_constructor_symbol(self):
        with self.assertRaises(ac.InvalidWordException):
            self.anagram = Anagram(self.word_symbol)

    def test_constructor_number(self):
        pass

    def test_constructor_capital(self):
        pass

if __name__ == '__main__':
    unittest.main()
