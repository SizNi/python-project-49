#!/usr/bin/env python3
from brain_games.scripts.cli import get_user_name
import random


def brain_prime():
    new_name = get_user_name()
    i = 0  # счетчик верных ответов
    result = True
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i <= 2 and result:  # цикл до 3 верных попыток или 1 ошибки
        prime, num = is_prime()
        print(f'Question: {num}')
        answer = input()
        answer = str(answer.lower())
        # цикл сравнения ответа игрока с правильным ответом
        if (answer == 'yes' and prime) or (answer == 'no' and not prime):
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        else:
            print(f"Wrong answer, {new_name}\nLets try again")
            result = False
    if result:
        print(f'Congratulations, {new_name}')
        return


def is_prime():
    num = random.randint(1, 1000)
    for elem in range(2, (num // 2) + 1):
        if num % elem == 0:
            return False, num
    return True, num
