class JumblePermutationsGenerator:
    @staticmethod
    def jumble(jumble_str):
        generator = JumblePermutationsGenerator(jumble_str)
        return generator.get_words()

    @staticmethod
    def accepted_letters(word):
        letters = {
            "a": True,
            "b": True,
            "c": True,
            "d": True,
            "e": True,
            "f": True,
            "g": True,
            "h": True,
            "i": True,
            "j": True,
            "k": True,
            "l": True,
            "m": True,
            "n": True,
            "o": True,
            "p": True,
            "q": True,
            "r": True,
            "s": True,
            "t": True,
            "u": True,
            "v": True,
            "w": True,
            "x": True,
            "y": True,
            "z": True
        }
        accepted_letters = []
        for letter in word.lower():
            if letter in letters:
                accepted_letters.append(letter)
        return accepted_letters

    def __init__(self, jumble_str):
        self.jumble_str = jumble_str
        self.letters = JumblePermutationsGenerator.accepted_letters(jumble_str)
        self.string_length = len(self.letters)
        self.word_list = {}
        self._setup_dictionary()

    def get_words(self):
        for jumble_length in range(2, self.string_length + 1):
            self.append_jumbles_in_length_of(jumble_length)
        return self.word_list.keys()

    def append_jumbles_in_length_of(self, pick):
        n = self.string_length
        indices = range(n)
        cycles = range(n, n - pick, -1)
        self._append_to_word_list(self.letters_to_word(indices[:pick]))
        while n:
            for i in reversed(range(pick)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    self._append_to_word_list(self.letters_to_word(indices[:pick]))
                    break
            else:
                return

    def letters_to_word(self, indices):
        letters = tuple(self.letters[i] for i in indices)
        return ''.join(letters)

    def _setup_dictionary(self):
        self.dictionary = {}
        american_words = open('all_english_words.txt', 'r')
        for word in american_words:
            formatted_word = JumblePermutationsGenerator.accepted_letters(word.strip())
            self.dictionary[''.join(formatted_word)] = True

    def _append_to_word_list(self, word):
        if self._is_word(word):
            self.word_list[word] = True

    def _is_word(self, word):
        return (word in self.dictionary)
