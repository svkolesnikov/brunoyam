x1 = int(input("Номер столбца 1-й клетки: "))
x2 = int(input("Номер строки 1-й клетки: "))
x3 = int(input("Номер столбца 2-й клетки: "))
x4 = int(input("Номер строки 2-й клетки: "))

if (0 < x1 < 9) & (0 < x2 < 9) & (0 < x3 < 9) & (0 < x4 < 9):
    if (x1 == x3) or (x2 == x4):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
