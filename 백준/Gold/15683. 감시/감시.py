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
result = 1e8


def enable_cctv(r, c, directions):
    _visited = set()
    for direction in directions:
        dr, dc = direction
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 6:
            if grid[nr][nc] == 0:
                _visited.add((nr, nc))
            nr += dr
            nc += dc

    return _visited


def solve(count, visited):
    global result
    if count == len(cctv):
        cmp = n * m - len(wall) - len(cctv) - len(visited)
        if cmp < result:
            result = cmp

        return

    r, c = cctv[count]
    for case in cases[grid[r][c]]:
        _visited = visited | enable_cctv(r, c, case)
        solve(count + 1, _visited)


solve(0, set())
print(result)
