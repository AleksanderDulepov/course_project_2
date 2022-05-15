from config import JSON_ADDRESS
import requests, random, inflect
from Word_class import Word
from Player_class import Player


def get_user():
    """
    Cоздает обьект класса Player
    """
    user = Player(input('Please, input players name:\n').strip())
    return user


def get_words():
    """
    Cоздает список обьектов класса Word из json
    """
    response = requests.get(JSON_ADDRESS).json()
    words_list = []
    for i in response:
        words_list.append(Word(i['word'], i['subwords']))
    random.shuffle(words_list)
    return words_list


def get_next_word(list):
    """
    Возвращает еще не сыгранное слово (обьект класса Word)
    """
    for word in list:
        if word.is_asked == None:
            return word
    print('We dont have any words for you, sorry')
    exit(0)


def another_game(choice):
    """
    Возвращает bool играем дальше или нет
    """
    return choice == 'yes'


def get_plural_eng(amount: int, word: str) -> str:
    '''
    This function to get english word's correct form that depends on the quantity
    '''
    p = inflect.engine()
    return f'{amount} {p.plural(word, amount)}'
