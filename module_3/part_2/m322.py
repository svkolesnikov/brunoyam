from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
# Индексы которые соответствуют максимальному значению
idI = 0
idJ = 0
val = -1
for i in range(n):
    for j in range(n):
        if (val < m[i][j]):
            idI = i
            idJ = j
            val = m[i][j]
print(f"Элемент с максимальным значением имеет индекс m[{idI}][{idJ}] \n")
print(f"Значение элемента {m[idI][idJ]}")