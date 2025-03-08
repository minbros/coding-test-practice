import sys

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            dist[i][j] = 0

for i in range(1, n + 1):
    print(*dist[i][1:])