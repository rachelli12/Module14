"""
Program: anagram_functions.py
Author: Rachel Li
Last date modified: 02/08/2020

The purpose of this program is to write anagram functions for GUI
"""
MIN_WORD_LENGTH = 2
#minimum length of word in output

class InvalidWordException(Exception):
    ''' invalid word exception '''
    pass

class Anagram_Functions(object):
    '''Anagram_Functions Class'''
    def __init__(self, letter='', final=False, depth=0):
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (word_characters.issuperset(letter)):
            raise InvalidWordException
        self.letter = letter
        self.final = final
        self.depth = depth
        self.dict = {}

    def add_letters(self, letters):
        """
        :param letters: represents letters in word
        :return: returns letters in dictionary with index
        """
        a = self
        for index, letter in enumerate(letters):
            #assign index to each iterable item
            if letter not in a.dict:
                a.dict[letter] = Anagram_Functions(letter, index==len(letters)-1, index+1)
            a = a.dict[letter]

    def anagram(self, letters):
        """
        :param letters: represents letters in word in set
        :return: return to _anagram function
        """
        alphabet = {}
        for letter in letters:
            alphabet[letter] = alphabet.get(letter, 0) + 1
        min_length = len(letters)
        return self._anagram(alphabet, [], self, min_length)

    def _anagram(self, alphabet, path, root, min_length):
        """
        :param alphabet: represents the set collection
        :param path: represents path
        :param root: represents root
        :param min_length: represents minimum length of word
        :return: return anagram
        """
        if self.final and self.depth >= MIN_WORD_LENGTH:
            word = ''.join(path)
            length = len(word.replace(' ', ''))
            if length >= min_length:
                yield word
            path.append(' ')
            for word in root._anagram(alphabet, path, root, min_length):
                yield word
            path.pop()
        for letter, a in self.dict.items():
            count = alphabet.get(letter, 0)
            if count == 0:
                continue
            alphabet[letter] = count - 1
            path.append(letter)
            for word in a._anagram(alphabet, path, root, min_length):
                yield word
            path.pop()
            alphabet[letter] = count

def load_dictionary(path):
    """
    :param path: represents wordlist.txt file
    :return: return anagrams of word into dictionary
    :rtype:
    """
    result = Anagram_Functions()
    for line in open(path, 'r'):
        word = line.strip().lower()
        result.add_letters(word)
    return result

def nagamar():
    """
    :return: returns anagram result
    """
    try:
        with open('wordlist.txt', 'r') as f:
            for dictionary in f.readline():
                if input != dictionary.strip().lower(): #strips and lowercase
                    break
                else:
                    letters = input('Enter letters: ')
                    letters = letters.lower()
                    letters = letters.replace(' ', '')
                count = 0
                for word in f.anagram(letters):
                    print(word)
                    count += 1
                print('%d results' % count) #print number of results
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print('Corrupt File')
    finally:
        f.close()

if __name__ == '__main__':
    words = load_dictionary('wordlist.txt')
    while True:
        letters = input('Enter letters: ')
        letters = letters.lower()
        letters = letters.replace(' ', '')
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (word_characters.issuperset(letters)):
            raise InvalidWordException
            break
        count = 0
        for word in words.anagram(letters):
            print(word)
            count += 1
        print ('%d results.' % count)
