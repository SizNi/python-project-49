def welcome_user():  # приветствие и ввод имени
    name = ''
    while name == '':
        print('whats your name, bro? ', end='')
        name = input()

    if __name__ == '__main__':
        print(f'Yo, {name.title()}!')
    return name
