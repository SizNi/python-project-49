#!/usr/bin/env python3
from random import randint
from brain_games.scripts.cli import get_user_name


def brain_even():
    new_name = get_user_name()  # получение имени из cli.py
    i = 0  # счетчик верных ответов
    # условие выхода из цикла если сменится на False в случае ошибки:
    result = True
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i <= 2 and result:  # цикл до 3 верных попыток или 1 ошибки
        number = randint(0, 1000)
        # проверка сгенерированного числа четность:
        if number % 2 == 0:
            even = True
        else:
            even = False
        print(f'Question: {number}')
        print('Your answer: ', end='')  # ввод ответа
        txt = input().lower()
        # цикл сравнения ответа игрока с правильным ответом
        if (even and txt == 'yes') or (not even and txt == 'no'):
            i += 1
            print('Correct!')
            result = True
        elif not even and txt == 'yes':  # ниже неверные ответы
            print(
                f"'{txt}' is wrong answer ;(."
                f"Correct answer was 'no'\nLet's try again, {new_name}!"
            )
            result = False
        else:
            print(
                f"'{txt}' is wrong answer ;(."
                f"Correct answer was 'yes'\nLet's try again, {new_name}!"
            )
            result = False
    if result:
        print(f'Congratulations, {new_name}!')
        return
