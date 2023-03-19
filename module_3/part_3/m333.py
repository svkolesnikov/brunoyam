ar = [56, 9, 11, 2]
#ar = [3, 81, 5]

# Переводим числа в строку
# Сортируем в обратном порядке
# Соединяем строки в одну и преобразовываем в число

arS = [str(i) for i in ar]
arS = sorted(arS, reverse=True)
val = int("".join(arS))

print(val)
