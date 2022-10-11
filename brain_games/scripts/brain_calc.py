#!/usr/bin/env python3
from brain_games.scripts.cli import get_user_name
import random
import operator


def brain_calc():
    new_name = get_user_name()
    i = 0  # счетчик верных ответов
    result = True
    result_random = 0
    print("What is the result of the expression?")
    while i <= 2 and result:  # цикл до 3 верных попыток или 1 ошибки
        result_random = random_count()
        answer = input()
        if answer == str(result_random):
            i += 1
            print(f'Correct, {new_name}!')
            result = True
        else:
            print(f"'{answer}' wrong. Correct was {result_random}")
            print(f"Lets try again, {new_name}!")
            result = False
    if result:
        print(f'Congratulations, {new_name}!')
        return


def random_count():
    ops = {'+': operator.add, 
           '-': operator.sub,
           '*': operator.mul}
    num1 = random.randint(0, 12)
    num2 = random.randint(1, 10)
    op = random.choice(list(ops.keys()))
    result_random = ops.get(op)(num1,num2)
    print(f'Question: {num1} {op} {num2}')
    return int(result_random)
