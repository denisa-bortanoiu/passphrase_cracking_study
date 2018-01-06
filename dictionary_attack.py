import string
from oracle import Oracle
from brute_force import BruteForce
from itertools import chain, product


class Dictionary(BruteForce):
    def __init__(self, min_words, max_words):
        self.min_words = min_words
        self.max_words = max_words
        self.alphabet = self.get_words()

    def read_text(self, text_file="test_extract.txt"):
        replace_punctuation = string.maketrans(",!?;:", "." * 5)
        replace_unknown_chars = string.maketrans("\"0123456789*/()#][$%^'_|&+=-", " "*28)
        word_list = []
        for line in open(text_file):
            line = line.lower()
            line = line.translate(replace_punctuation).translate(replace_unknown_chars).replace(".", " . ")
            word_list.extend(line.split())
        return word_list

    def get_words(self):
        words = self.read_text()
        words = list(set(words))
        print "Completed the dictionary"
        return words

    def guesses(self):
        return (''.join(candidate)
                for candidate in chain.from_iterable(product(self.alphabet, repeat=i)
                                                     for i in range(self.min_words, self.max_words)))


def test_me():
    test_example = Dictionary(1, 5)
    test_example.attack(Oracle("thisisa"))

test_me()