import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cctv = []
wall = []
for i in range(n):
    for j in range(m):
        value = grid[i][j]
        if value == 6:
            wall.append((i, j))
        elif value != 0:
            cctv.append((i, j))

cases = {
    1: [((1, 0),), ((0, 1),), ((-1, 0),), ((0, -1),)],
    2: [((1, 0), (-1, 0)), ((0, 1), (0, -1))],
    3: [((1, 0), (0, 1)), ((1, 0), (0, -1)), ((0, 1), (-1, 0)), ((-1, 0), (0, -1))],
    4: [((1, 0), (0, 1), (-1, 0)), ((1, 0), (0, 1), (0, -1)), ((1, 0), (-1, 0), (0, -1)), ((0, 1), (-1, 0), (0, -1))],
    5: [((1, 0), (0, 1), (-1, 0), (0, -1))]
}
list_directions = []
result = 1e8


def enable_cctv(r, c, directions, _grid):
    for direction in directions:
        dr, dc = direction
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < m and _grid[nr][nc] != 6:
            if _grid[nr][nc] == 0:
                _grid[nr][nc] = '#'
            nr += dr
            nc += dc


def solve(count):
    global result
    if count == len(cctv):
        grid_copy = copy.deepcopy(grid)
        for coord, directions in zip(cctv, list_directions):
            r, c = coord
            enable_cctv(r, c, directions, grid_copy)

        cmp = 0
        for row in grid_copy:
            cmp += row.count(0)

        if cmp < result:
            result = cmp

        return

    r, c = cctv[count]
    for case in cases[grid[r][c]]:
        list_directions.append(case)
        solve(count + 1)
        list_directions.pop()


solve(0)
print(result)
