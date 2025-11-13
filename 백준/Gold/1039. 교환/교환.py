from collections import defaultdict

n, k = map(int, input().split())
length = len(str(n))
visited = defaultdict(set)
visited[0].add(str(n))
result = -1
for depth in range(k):
    for num in visited[depth]:
        for i in range(length):
            for j in range(i + 1, length):
                if i == 0 and num[j] == '0':
                    continue

                swapped = list(num)
                swapped[i], swapped[j] = swapped[j], swapped[i]
                new = ''.join(swapped)
                visited[depth + 1].add(new)

for num in visited[k]:
    result = max(result, int(num))

print(result)
