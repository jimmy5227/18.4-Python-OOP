"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    ...

    def __init__(self, file):
        self.list = []
        self.parse(open(file, 'r'))
        print(f'{len(self.list)} words read')

    def parse(self, file):
        for line in file:
            self.list.append(line.strip())

    def random(self):
        return choice(self.list)
