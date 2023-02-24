password = input('Пароль:')
while not((len(password) >= 8) & (password.upper() != password) & (password.lower() != password)):
    print("FAIL")
    password = input('Пароль:')
print("OK")
