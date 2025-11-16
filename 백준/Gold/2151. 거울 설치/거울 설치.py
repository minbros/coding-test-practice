import sys
from collections import deque

input = sys.stdin.readline
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    queue = deque([(0, UP, doors[0]), (0, RIGHT, doors[0]), (0, DOWN, doors[0]), (0, LEFT, doors[0])])
    visited = [[False] * n for _ in range(n)]
    visited[doors[0][0]][doors[0][1]] = True
    while queue:
        depth, direction, (x, y) = queue.popleft()
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
            if grid[nx][ny] == '#':
                return depth

            if grid[nx][ny] == '!' and not visited[nx][ny]:
                queue.append((depth + 1, (direction + 1) % 4, (nx, ny)))
                queue.append((depth + 1, (direction + 3) % 4, (nx, ny)))
                visited[nx][ny] = True

            nx += dx
            ny += dy

    return -1


n = int(input())
grid = [input().strip() for _ in range(n)]
doors = [(r, c) for c in range(n) for r in range(n) if grid[r][c] == '#']
print(solve())
