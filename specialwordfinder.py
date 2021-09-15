from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):

    def __init__(self, file):
        super().__init__(file)

    def parse(self, file):
        for line in file:
            if line.startswith("#") or line.startswith("\n"):
                None
            else:
                self.list.append(line.strip())
