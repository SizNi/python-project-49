#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
import random

def brain_prime():
    new_name = main().title()
    i = 0  # счетчик верных ответов
    result = True
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i <= 2 and result == True:  # цикл до 3 верных попыток или 1 ошибки
        prime, num = is_prime()
        print(f'Question: {num}')
        answer = input()
        answer = str(answer.lower())
        # цикл сравнения ответа игрока с правильным ответом
        if (answer == 'yes' and prime == True) or (answer == 'no' and prime == False) :
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        else:
            print(f"А вот нетушки, совсем неверно, надо переделать, товарищ {new_name}")
            result = False
    if result == True:
        print(f'Congratulations, {new_name}')
        return


def is_prime():
    num = random.randint(1,1000)
    for elem in range(2,(num//2) + 1):
        if num % elem == 0:
            return False, num
    return True, num