"""
Program: anagram_class.py
Author: Rachel Li
Last date modified: 29/07/2020

The purpose of this program is to write class with exception for anagram
"""
class InvalidWordException(Exception):
    ''' invalid word exception '''
    pass


class Anagram():
    """Anagram class"""
    def __init__(self, word):
        """Anagram Constructor"""
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (word_characters.issuperset(word)):
            raise InvalidWordException
        self.word = word
        self.sorted_anagram = self.arrange_letter()

    def arrange_letter(self):
        """
        :return: sorted result of letters
        """
        lower_case = self.word.strip().lower()
        alphabet = sorted(list(lower_case))
        return ''.join(sorted(alphabet))

    def sort_anagram(self):
        return self.sorted_anagram

    def __str__(self):
        return f'Word: {self.word}, Anagram: {self.sorted_anagram}'

