import sys
from collections import deque

input = lambda: sys.stdin.readline()


def bfs():
    global fires

    max_d = 0
    while queue:
        x, y, d = queue.popleft()
        if d > max_d:
            fires = move_fire()
            max_d += 1

        if fire_visited[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx in (-1, r) or ny in (-1, c):
                return d + 1

            if in_bound(nx, ny) and not visited[nx][ny] and grid[nx][ny] == '.' and not fire_visited[nx][ny]:
                queue.append((nx, ny, d + 1))
                visited[nx][ny] = True

    return 'IMPOSSIBLE'


def move_fire():
    new_fires = []
    for x, y in fires:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bound(nx, ny) and grid[nx][ny] != '#' and not fire_visited[nx][ny]:
                new_fires.append((nx, ny))
                fire_visited[nx][ny] = True

    return new_fires


def in_bound(nx, ny):
    return 0 <= nx < r and 0 <= ny < c


r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
queue = deque()
fires = []
visited = [[False] * c for _ in range(r)]
fire_visited = [[False] * c for _ in range(r)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'J':
            queue.append((i, j, 0))
            visited[i][j] = True

        elif grid[i][j] == 'F':
            fires.append((i, j))
            fire_visited[i][j] = True

print(bfs())
