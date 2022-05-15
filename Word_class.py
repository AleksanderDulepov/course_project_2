class Word:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords
        self.length_subwords = len(self.subwords)
        self.is_asked = None
        self.early_exit = False

    def __repr__(self):
        return f'This is a Word class object {self.word}'

    def add_to_used_words(self):
        self.is_asked = True

    def check_answer(self, answer):
        return answer in self.subwords

    def check_early_exit(self, answer):
        self.early_exit = answer == 'stop'
        return self.early_exit
