# l - массив в котором осуществялеся поиск
l = [1, 3, 4, 6, 8, 11, 12, 324, 566, 3453, 6565, 56756, 354, 87, 3434, 86]
l.sort()


val = int(input("Введите число:"))

left = 0
right = len(l)-1
middle = len(l) // 2

while (l[middle] != val) and (right-left > 1):
    if  val < l[middle]: # Искомое число меньше середины отрезка
        right = middle
    else:
        left = middle

    middle = left + (right - left) // 2

if (right-left <= 1):
    print("Число не найдено")
else:
    print(f"Искомое число имеет индекс: {middle}")




