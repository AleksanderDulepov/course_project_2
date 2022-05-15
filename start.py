from utils import *

user = get_user()
list_objects_words = get_words()  # список обьектов-слов
print(f'Hello, {user.name}!')
while True:
    word_in_list = get_next_word(list_objects_words)  # выбор еще не сыгранного слова
    term_info = word_in_list.add_to_used_words()  # обновляет self.asked
    current_asked_word = word_in_list.word
    amount_words_to_guess = word_in_list.length_subwords
    print(f'Lets compose {amount_words_to_guess} words with letters from word "{current_asked_word}"\n'
          f'Words should consist more than 3 letters\n'
          f'You have to guess all words or input "stop" to finish the game\n'
          f'Lets start! What is your first word?')
    user.make_history_list(current_asked_word)  # добавление слова в список player.history_words
    user.clean_previous_replies()  # очистка буфера после очередной записи

    for attempt in range(amount_words_to_guess):
        user_answer = input().strip()
        if word_in_list.check_early_exit(user_answer):
            break
        result_check = word_in_list.check_answer(user_answer)  # проверка правильности ответа
        user.add_to_stat_dict(attempt + 1, result_check)  # добавление результата в словарь player.stat_dict
        if result_check:
            print('Right!')
        else:
            print('Wrong!')

    amount = user.get_amount_right_answer(current_asked_word)

    if word_in_list.early_exit:
        print(f'You have complited the game\n'
              f"You guess {get_plural_eng(amount, 'word')}.")
    else:
        print(f'You is all. Game over!\n'
              f"You guess {get_plural_eng(amount, 'word')}.")
    is_success_saving = user.save_results()
    if is_success_saving:
        print(f'Results were successfully saved to file results_{user.name}.json.')
    else:
        print('Произошла ошибка, сохранение результатов в файл не было завершено!')
        print('Something wrong! Saving wasnt successfully!')

    if not another_game(input('Do you want to play once?\nPlease, input yes or no\n').strip()):
        break
