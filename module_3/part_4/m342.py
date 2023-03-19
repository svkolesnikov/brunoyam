def register(login, passwd):
    import json

    try:
        with open('user.json', 'r') as f:
            data = json.load(f)
    except:
        data = []

    # Проверяем существует ли пользователь
    for rec in data:
        if (rec['login'] == login):
            print("Пользователь существует")
            return -1

    # Сохраняем, если не существует
    reg = {'login': login, 'password': passwd}
    data.append(reg)
    with open('user.json', 'w') as f:
        json.dump(data, f)
        print("Пользователь добавлен")
    return 0

print('Регистрация пользователя')
login = input('Введите логин: ')
passwd = input('Введите пароль: ')

register(login, passwd)
