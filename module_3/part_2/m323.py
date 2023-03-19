d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
d2 = {}
for key, val in d.items():
    d2[val] = key
print(d2)

