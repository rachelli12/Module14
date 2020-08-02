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
        a = self
        for index, letter in enumerate(letters):
            if letter not in a.dict:
                a.dict[letter] = Anagram_Functions(letter, index==len(letters)-1, index+1)
            a = a.dict[letter]

    def anagram(self, letters):
        tiles = {}
        for letter in letters:
            tiles[letter] = tiles.get(letter, 0) + 1
        min_length = len(letters)
        return self._anagram(tiles, [], self, min_length)

    def _anagram(self, tiles, path, root, min_length):
        if self.final and self.depth >= MIN_WORD_LENGTH:
            word = ''.join(path)
            length = len(word.replace(' ', ''))
            if length >= min_length:
                yield word
            path.append(' ')
            for word in root._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
        for letter, node in self.dict.items():
            count = tiles.get(letter, 0)
            if count == 0:
                continue
            tiles[letter] = count - 1
            path.append(letter)
            for word in node._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
            tiles[letter] = count

def load_dictionary(path):
    result = Anagram_Functions()
    for line in open(path, 'r'):
        word = line.strip().lower()
        result.add_letters(word)
    return result

def main():
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
        if not letters:
            break
        count = 0
        for word in words.anagram(letters):
            print(word)
            count += 1
        print ('%d results.' % count)
