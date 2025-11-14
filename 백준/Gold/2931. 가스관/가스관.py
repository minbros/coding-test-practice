import sys
from collections import deque

input = sys.stdin.readline
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

pipes = {
    '|': {UP, DOWN},
    '-': {LEFT, RIGHT},
    '+': {UP, DOWN, LEFT, RIGHT},
    '1': {DOWN, RIGHT},
    '2': {UP, RIGHT},
    '3': {LEFT, UP},
    '4': {LEFT, DOWN}
}


def find_erased_area(start):
    queue = deque([start])
    visited = [[False for _ in range(c)] for _ in range(r)]
    while queue:
        x, y = queue.popleft()
        directions = []
        if grid[x][y] in ('M', 'Z'):
            directions = [UP, DOWN, LEFT, RIGHT]
        elif grid[x][y] != '.':
            directions = pipes[grid[x][y]]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if grid[x][y] not in ('M', 'Z') and grid[nx][ny] == '.':
                    return nx, ny

                if grid[nx][ny] != '.':
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return -1, -1


def isolated_region(x, y):
    if (x, y) not in ('M', 'Z'):
        return False

    for dx, dy in [UP, DOWN, LEFT, RIGHT]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < r and 0 <= ny < c) and (grid[nx][ny] == '.' or broken_pipe(dx, dy, nx, ny)):
            return False

    return True


def broken_pipe(dx, dy, nx, ny):
    return grid[nx][ny] in pipes.keys() and (-dx, -dy) in pipes[grid[nx][ny]]


def find_correct_pipe(x, y):
    dirs = set()
    for dx, dy in [UP, DOWN, LEFT, RIGHT]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != '.':
            if broken_pipe(dx, dy, nx, ny) or isolated_region(nx, ny):
                dirs.add((dx, dy))

    for key in pipes.keys():
        if pipes[key] == dirs:
            return key

    return None


r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]
moscow = zagreb = (0, 0)
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'M':
            moscow = (i, j)
        elif grid[i][j] == 'Z':
            zagreb = (i, j)

a, b = find_erased_area(moscow)
if (a, b) == (-1, -1):
    (a, b) = find_erased_area(zagreb)

print(a + 1, b + 1, find_correct_pipe(a, b))
