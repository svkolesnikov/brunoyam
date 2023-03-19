def login_function(login, passwd):
    import json

    flgAuth = False
    try:
        with open('user.json', 'r') as f:
            data = json.load(f)
    except:
        data = []

    # Проверяем существует ли пользователь
    for rec in data:
        if (rec['login'] == login) & (rec['password'] == passwd):
            flgAuth = True
            break
    if flgAuth:
        print("Пользователь авторизован")
    else:
        print("Неверная пара логин и пароль")
    pass


print('Авторизация пользователя')
login = input('Введите логин: ')
passwd = input('Введите пароль: ')

login_function(login, passwd)
