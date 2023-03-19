n = int(input("Введите целое число"))
summa = 0
while (n >= 1):
    summa += n % 10
    n = int(n / 10)

print(f"Сумма = {summa}")
