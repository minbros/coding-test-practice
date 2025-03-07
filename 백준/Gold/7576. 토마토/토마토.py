import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomatoes = []
for _ in range(n):
    tomatoes.append(list(map(int, input().split())))

count = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j, 0))
        elif tomatoes[i][j] == -1:
            count += 1

d = 0
visited = [[False for _ in range(m)] for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
while count < m * n and queue:
    y, x, d = queue.popleft()
    if not visited[y][x]:
        count += 1
        visited[y][x] = True
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if m > nx >= 0 and n > ny >= 0 == tomatoes[ny][nx]:
                queue.append((ny, nx, d + 1))

if count == m * n:
    print(d)
else:
    print(-1)