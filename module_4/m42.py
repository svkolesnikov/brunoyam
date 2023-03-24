# Сортировка методом вставки
def sortInsert():
    ar = l
    for i in range(1, len(ar)):
        j = i
        while (j > 0) & (ar[j] < ar[j-1]):
            ar[j-1], ar[j] = ar[j], ar[j-1]
            j -= 1
    pass


l = [8, 1, 5, 2, 6, 9, 3]
print(l)
sortInsert()
print(l)
