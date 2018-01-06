import string


class ExtractNgrams(object):
    def __init__(self):
        self.n = 4
        self.text_file = "test_extract.txt"
        self.word_list = []
        self.ngrams = {}

    def read_text(self):
        replace_punctuation = string.maketrans(",!?;:", "." * 5)
        replace_unknown_chars = string.maketrans("\"0123456789*/()#][$%^'_|&+=-", " "*28)
        print self.text_file
        for line in open(self.text_file):
            line = line.lower()
            line = line.translate(replace_punctuation).translate(replace_unknown_chars).replace(".", " . ")
            self.word_list.extend(line.split())

    def get_ngrams(self):
        self.read_text()
        for elem in zip(*[self.word_list[i:] for i in range(self.n)]):
            if elem[:2] == ('.', '.') or elem[1:3] == ('.', '.') or elem[2:] == ('.', '.'):
                continue
            self.ngrams[elem] = self.ngrams.get(elem, 0) + 1

        with open("ngrams_extracted.txt", "w") as f:
            for key, value in sorted(self.ngrams.iteritems()):
                f.write("%s %s %s %s %s\n" % (key[0], key[1], key[2], key[3], value))


def test_me():
    test_example = ExtractNgrams()
    test_example.get_ngrams()


test_me()
