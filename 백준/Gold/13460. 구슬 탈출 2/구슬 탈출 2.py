import sys
from collections import deque

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def move(_coord, _other_coord, _direction):
    r, c = _coord
    dr, dc = list_direction[_direction]
    nr, nc = r + dr, c + dc
    while grid[nr][nc] != '#' and (nr, nc) != _other_coord:
        if grid[nr][nc] == 'O':
            return None

        nr += dr
        nc += dc

    return nr - dr, nc - dc


def move_both(_coord_r, _coord_b, _direction, is_r_first: bool):
    if is_r_first:
        _coord_r = move(_coord_r, _coord_b, _direction)
        _coord_b = move(_coord_b, _coord_r, _direction)
    else:
        _coord_b = move(_coord_b, _coord_r, _direction)
        _coord_r = move(_coord_r, _coord_b, _direction)

    return _coord_r, _coord_b


input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
list_direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
coord_b, coord_r = (0, 0), (0, 0)
for i in range(n):
    row = input()
    if "B" in row:
        coord_b = (i, row.index("B"))

    if "R" in row:
        coord_r = (i, row.index("R"))

    grid.append(row)

q = deque()
q.append((coord_r, coord_b, 0))
visited = [[[[False]* m for _ in range(n)] for __ in range(m)] for ___ in range(n)]
visited[coord_r[0]][coord_r[1]][coord_b[0]][coord_b[1]] = True
while q:
    coord_r, coord_b, depth = q.popleft()
    if depth >= 10:
        continue

    coords = [move_both(coord_r, coord_b, UP, coord_r[0] <= coord_b[0]),
              move_both(coord_r, coord_b, RIGHT, coord_r[1] >= coord_b[1]),
              move_both(coord_r, coord_b, DOWN, coord_r[0] >= coord_b[0]),
              move_both(coord_r, coord_b, LEFT, coord_r[1] <= coord_b[1])]

    for tmp_coord_r, tmp_coord_b in coords:
        if tmp_coord_b is None:
            continue

        if tmp_coord_r is None:
            print(depth + 1)
            quit()

        if not visited[tmp_coord_r[0]][tmp_coord_r[1]][tmp_coord_b[0]][tmp_coord_b[1]]:
            visited[tmp_coord_r[0]][tmp_coord_r[1]][tmp_coord_b[0]][tmp_coord_b[1]] = True
            q.append((tmp_coord_r, tmp_coord_b, depth + 1))

print(-1)
