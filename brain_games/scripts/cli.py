def welcome_user():  # приветствие и ввод имени
    name = ''
    while name == '':
        print('May i have your name?', end = ' ')
        name = input()
        print(f'Hello, {name.title()}!')
    return name
