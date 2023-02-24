a = float(input("число 1:"))
b = float(input("число 2:"))
max = (a > b) * a + (a < b) * b
print(max)
