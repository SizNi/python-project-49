#!/usr/bin/env python3
from brain_games.scripts.cli import welcome_user


def main():
    # print('poetry run brain_games')
    print('Welcome to the Brain games!')
    name = welcome_user()
    print(f'Yo, {name.title()}!')

    if __name__ == '__main__':
        main()
    return name
