#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
import math
import random

def brain_gcd():
    new_name = main().title()
    i = 0  # счетчик верных ответов
    result = True
    print("Find the greatest common divisor of given numbers.")
    while i <= 2 and result == True:  # цикл до 3 верных попыток или 1 ошибки
        gcd = gcd_enter()
        answer = input()
        if int(answer) == gcd:
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {gcd}\nLets try again, {new_name}!")
            result = False
    if result == True:
        print(f'Congratulations, {new_name}')
        return

def gcd_enter():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(f'Question: {num1} and {num2}')
    gcd_result = math.gcd(num1, num2)
    return gcd_result
