def area(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c))
    if (S >= 0):
        return S ** 0.5
    else:
        return -1


a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
S = area(a, b, c)
if S >= 0:
    print(f"Площадь треугольника {S}")
else:
    print("Неверно указаны длины сторон")
