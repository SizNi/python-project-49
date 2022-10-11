def welcome_user():  # приветствие и ввод имени
    name = ''
    while name == '':
        name = input()
        return name


def get_user_name():
    print('Welcome to the Brain Games!')
    print('May I have your name?', end=' ')
    name = welcome_user().title()
    print(f'Hello, {name}!')
    return name
