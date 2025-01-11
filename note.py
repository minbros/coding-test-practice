arr = [['a', 1], ['b', 2], ['a', 3]]
dic = {}

for item in arr:
    key, value = item
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = [value]

s = 0
for arr in dic.values():
    s += len(arr)

print(s)