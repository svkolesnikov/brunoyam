l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l_unic = []
l_rep = []
for v in l:
    if (v not in l_unic):
        l_unic.append(v)
    else:
        l_rep.append(v)
print(f"Исходный список:{l}")
print(f"Повторы:{l_rep}")


