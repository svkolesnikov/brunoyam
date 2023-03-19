x = float(input("Вклад в руб:"))
y = float(input("Желаемая сумма:"))
p = float(input("Процент по вкладу, %:"))

p = p / 100
cnt = 0
while (x <= y ):
    x_old = x
    x = int(x*(1+p))
    if (x <= x_old):
        break
    cnt += 1

if (cnt > 0):
    print(f"Вклад нужно держать: {cnt} лет")
elif(x <= x_old):
    print("Слишком маленькая ставка по вкладу")
else:
    print("Вы уже достигли желаемую сумму")


