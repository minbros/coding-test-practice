import sys

input = lambda: sys.stdin.readline()
INF = float('inf')

v, e = map(int, input().split())
roads = [[INF] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    roads[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

answer = INF
for i in range(v):
    answer = min(answer, roads[i][i])

print(-1 if answer == INF else answer)
