class Oracle(object):
    def __init__(self, secret):
        self.__secret = secret

    def verify_passphrase(self, guess):
        return guess == self.__secret
