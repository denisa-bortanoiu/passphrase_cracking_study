import time
from oracle import Oracle
from itertools import chain, product


class BruteForce(object):
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def guesses(self):
        return (''.join(candidate)
                for candidate in chain.from_iterable(product(self.alphabet, repeat=i)
                                                     for i in range(self.min_length, self.max_length)))

    def attack(self, oracle):
        start = time.time()
        print "Starting attack..."
        for guess in self.guesses():
            if oracle.verify_passphrase(guess):
                end = time.time()
                print "Found it: %s" % guess
                print end - start
                return

        print "Could not find the passphrase!"


def test_me():
    test_example = BruteForce(4, 12)
    test_example.attack(Oracle("tester"))


if __name__ == '__main__':
    test_me()
