import json


class Player:
    def __init__(self, name):
        self.name = name.strip()
        self.history_words = []  # список слов, на которые юсер уже отвечал
        self.stat_dict = {}  # словарь статы (словарь из словарей с результатами ответов)
        self.dict_ = {}  # технологический буфер

    def __repr__(self):
        return f"This is a Player class object {self.name}"

    def make_history_list(self, word):
        self.history_words.append(word)

    def clean_previous_replies(self):  # очищение буфера после очередного слова
        self.dict_ = {}

    def add_to_stat_dict(self, attempt, result):  # создаем словарь с результатами
        self.dict_[attempt] = result
        self.stat_dict[self.history_words[-1]] = self.dict_

    def get_amount_right_answer(self, word):
        try:
            dict_with_results = self.stat_dict[word]
            amount_right_answer = list(dict_with_results.values()).count(True)
            return amount_right_answer
        except:  # в случае stop до первого ответа
            return 0

    def save_results(self):
        try:
            with open(f'results_{self.name}.json', 'w') as file:
                json.dump(self.stat_dict, file, ensure_ascii=False)
                return True
        except:
            return False
