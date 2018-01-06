import time
from oracle import Oracle


class State(object):
    def __init__(self, n, state):
        self.n = n
        self.current = state[:-2]
        self.possible = {state[-2]: state[-1]}

    def add_possible(self, next_state, occurrence):
        self.possible.update({next_state: occurrence})

    def __repr__(self):
        return str(self.current) + ': ' + str(self.possible)


class MarkovChains(object):
    def __init__(self, min_length, max_length, n=4, threshold=15):
        self.n = n
        self.states = []
        self.threshold = threshold
        self.min_length = min_length
        self.max_length = max_length

    def read_states(self, stats_file="ngrams_extracted.txt"):
        for line in open(stats_file):
            state = line.split()
            if int(state[self.n]) < self.threshold:
                continue

            try:
                if self.states[len(self.states) - 1].current == state[:-2]:
                    self.states[len(self.states) - 1].add_possible(state[-2], state[-1])
                else:
                    self.states.append(State(self.n, line.split()))
            except IndexError:
                self.states.append(State(self.n, line.split()))

    def get_next_state(self, current_state, word):
        next = current_state.current[1:] + [word]
        for state in self.states:
            if state.current == next:
                return state
        return None

    def verify_guess(self, guess, oracle):
        # print guess
        length = len(guess)
        if length > self.max_length:
            return False
        if self.min_length <= length:
            if oracle.verify_passphrase(guess):
                print "Found it: %s" % guess
                return True
        return False

    def generate(self, oracle, current_state, guess=''):
        if len(guess) > self.max_length:
            return False
        if self.verify_guess(guess, oracle):
            return True

        for word, occurences in sorted(current_state.possible.iteritems(),
                                       key=lambda (k, v): (v, k),
                                       reverse=True):
            new_guess = guess + (word if word != '.' else '')

            next_state = self.get_next_state(current_state, word)
            if next_state:
                if self.generate(oracle, next_state, new_guess):
                    return True
            else:
                if self.verify_guess(new_guess, oracle):
                    return True

        return False

    def attack(self, oracle):
        print "Starting attack..."
        start = time.time()
        for state in self.states:
            if self.generate(oracle, state, ''.join([word for word in state.current if word != '.'])):
                end = time.time()
                print end - start
                return
        print time.time() - start
        print "Could not crack the passphrase"


def test_me():
    test = MarkovChains(4, 20)
    test.read_states()
    test.attack(Oracle("onthefieldofbattle"))

test_me()