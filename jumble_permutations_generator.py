class JumblePermutationsGenerator:
    def __init__(self, jumble_str):
        self.jumble_str = jumble_str
        self.letters = tuple(self.jumble_str)
        self.string_length = len(self.letters)
        self._setup_dictionary()

    def jumbles_in_length_of(self, pick):
        n = self.string_length
        indices = range(n)
        cycles = range(n, n - pick, -1)
        word_list = []
        self._append_to_word_list(word_list, self.letters_to_word(indices[:pick]))
        while n:
            for i in reversed(range(pick)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    self._append_to_word_list(word_list, self.letters_to_word(indices[:pick]))
                    break
            else:
                return word_list

    def letters_to_word(self, indices):
        letters = tuple(self.letters[i] for i in indices)
        return ''.join(letters)

    def _setup_dictionary(self):
        self.dictionary = {}
        american_words = open('english-words.10', 'r')
        for word in american_words:
            self.dictionary[word.strip()] = True

    def _append_to_word_list(self, word_list, word):
        if self._is_word(word):
            word_list.append(word)

    def _is_word(self, word):
        return (word in self.dictionary)
