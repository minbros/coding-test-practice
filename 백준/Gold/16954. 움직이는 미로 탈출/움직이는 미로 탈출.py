import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs():
    queue = deque([(0, 7, 0)])
    visited = defaultdict(set)
    time = 0
    while queue:
        depth, x, y = queue.popleft()
        if depth > time:
            move_walls()
            time += 1

        if (x, y) in walls:
            continue

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if (nx, ny) == (0, 7):
                    return 1

                if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in walls and (nx, ny) not in visited[depth + 1]:
                    queue.append((depth + 1, nx, ny))
                    visited[depth + 1].add((nx, ny))

    return 0


def move_walls():
    global walls
    new_walls = set()
    for x, y in walls:
        if x + 1 < 8:
            new_walls.add((x + 1, y))

    walls = new_walls


grid = [input().strip() for _ in range(8)]
walls = {(i, j) for j in range(8) for i in range(8) if grid[i][j] == '#'}
print(bfs())
