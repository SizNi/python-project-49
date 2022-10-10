#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
import random
import operator

def brain_progression():
    new_name = main().title()
    i = 0  # счетчик верных ответов
    result = True
    progress = []
    print("What number is missing in the progression?")
    while i <= 2 and result == True:  # цикл до 3 верных попыток или 1 ошибки
        progress = create_progression()
        know_number = random.randint(0,len(progress)-1)  # выбор убранного знака
        saved_know_number = progress[know_number]  # запомнили верный ответ
        progress[know_number] = '...'
        progress_to_show = (' '.join(map(str, progress)))
        print(f'Question: {progress_to_show}')
        answer = input()
        # цикл сравнения ответа игрока с правильным ответом
        if answer == str(saved_know_number):
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {saved_know_number}\nLets try again, {new_name}!")
            result = False
    if result == True:
        print(f'Congratulations, {new_name}')
        return

def create_progression():
    coef_progr = random.randint(1,7)  # коэффициент увеличения прогресси
    coef_len = random.randint(5,20)  # случайно определяется длина прогрессии
    progression = [random.randint(0,5)] # определение стартового значения прогрессии
    i = 1
    a = 0
    while i <= coef_len:
        a = progression[i-1] + coef_progr
        progression.append(a)
        i += 1
    return progression
