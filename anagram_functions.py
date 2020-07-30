"""
Author: Rachel Li
Program: anagram_functions.py
Last date modified: 29/07/2020

The purpose of this program is to write functions for anagram.
"""
import os
from collections import Counter
from anagram_class import Anagram
import sys
import time

def check_word(user):
    """Check if word is in English"""
    english_word = True
    try:
        #open loaded dictionary file with all words
        with open('wordlist.txt', 'r') as f:
            for dictionary in f.readlines():
                #lowercase
                if user == dictionary.strip().lower():
                    english_word = True
                return english_word
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print("Corrupt File")
    finally:
        f.close()

def check_input(user):
    word = user.strip().lower()
    try:
        anagram_object = Anagram(word)
    except ValueError:
        print("Invalid")
    else:
        if not check_word(word):
            print("Not a word")
        else:
            return_anagrams(anagram_object.sort_anagram())

def create_dictionary(word):
    """Sort letters and create dictionary"""
    with open ('wordlist.txt', 'a+') as f:
        anagram_dictionary = {}
    for word in f.readlines():
        input = word.strip().lower()
        alphabet = sorted(list(input))
        if alphabet in anagram_dictionary:
            anagram_dictionary[alphabet].append(input)
        else:
            anagram_dictionary[alphabet] = [input]
    f.close()


#take in any string as parameter
#return list containing all anagrams
def return_anagrams(letters: str) -> list:
    global dictionary
    letters = letters.lower()
    letters_count = Counter(letters)

    anagrams = set()
    for word in dictionary:
        #check if all unique letters in word are scrambled
        if not set(word) - set(letters):
            check_word = set()
            for k, v in Counter(word).items():
                #check if count of each letter less than or equal to count
                #in scrambled letter input
                if v <= letters_count[k]:
                    check_word.add(k)
            if check_word == set(word):
                #check if equal to letters in word of dictionary
                anagrams.add(word)
    anagrams.remove('')
    return sorted(list(anagrams), key=lambda x: len(x))

if __name__ == '__main__':
    print(check_word("racecar"))


