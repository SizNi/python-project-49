def welcome_user():
    name = ''
    while name == '':
        print('whats your name, bro? ', end='')
        name = input()
        print(f'Yo, {name.title()}!')
