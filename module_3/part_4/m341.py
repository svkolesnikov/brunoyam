def register(login, passwd):
    import json
    reg = {'login': login, 'password': passwd}

    try:
        with open('user.json', 'r') as f:
            data = json.load(f)
    except:
        data = []

    data.append(reg)

    with open('user.json', 'w') as f:
        json.dump(data, f)
    pass


print('Регистрация пользователя')
login = input('Введите логин: ')
passwd = input('Введите пароль: ')

register(login, passwd)
