a = int(input("число 1: "))
b = int(input("число 2: "))
c = int(input("число 3: "))
if (a == b) & (a == c):
    print('3')
elif (a == b) | (a == c) | (c == b):
    print('2')
else:
    print('0')
