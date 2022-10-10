#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import main


def brain_even():
    new_name = main().title()  # получение имени из cli.py
    i = 0  # счетчик верных ответов
    # условие выхода из цикла если сменится на False в случае ошибки:
    result = True
    print("Answer 'yes' if the number is even, otherwise answer 'no'")
    while i <= 2 and result == True:  # цикл до 3 верных попыток или 1 ошибки
        number = randint(0, 1000)
        # проверка сгенерированного числа четность:
        if number % 2 == 0:
            even = True
        else:
            even = False
        print(f'Question: {number}')
        txt = input('your answer: ')  # ввод ответа
        txt = txt.lower()
        # цикл сравнения ответа игрока с правильным ответом
        if (even == True and txt == 'yes') or (even == False and txt == 'no'):
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        elif even == False and txt == 'yes':  # ниже неверные ответы
            print(f"'{txt}' is wrong answer ;(. Correct answer was 'no'\nLets try again, {new_name}!")
            result = False
        else:
            print(f"'{txt}' is wrong answer ;(. Correct answer was 'yes'\nLets try again, {new_name}!")
            result = False
    if result == True:
        print(f'Congratulations, {new_name}')
        return
