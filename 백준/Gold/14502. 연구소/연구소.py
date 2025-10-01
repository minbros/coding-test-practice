import sys
import itertools
import copy
from collections import deque

input = sys.stdin.readline


def bfs(_labs):
    value = 0
    _queue = copy.deepcopy(queue)
    _visited = copy.deepcopy(visited)
    while _queue:
        y, x = _queue.popleft()
        if y - 1 >= 0 and not _visited[y - 1][x] and _labs[y - 1][x] == 0:
            _queue.append((y - 1, x))
            _visited[y - 1][x] = True
            _labs[y - 1][x] = 2

        if y + 1 < n and not _visited[y + 1][x] and _labs[y + 1][x] == 0:
            _queue.append((y + 1, x))
            _visited[y + 1][x] = True
            _labs[y + 1][x] = 2

        if x - 1 >= 0 and not _visited[y][x - 1] and _labs[y][x - 1] == 0:
            _queue.append((y, x - 1))
            _visited[y][x - 1] = True
            _labs[y][x - 1] = 2

        if x + 1 < m and not _visited[y][x + 1] and _labs[y][x + 1] == 0:
            _queue.append((y, x + 1))
            _visited[y][x + 1] = True
            _labs[y][x + 1] = 2

    for row in _labs:
        value += row.count(0)

    return value


n, m = map(int, input().split())
labs = []
queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
for r in range(n):
    l = list(map(int, input().split()))
    for c in range(m):
        if l[c] == 2:
            queue.append((r, c))
            visited[r][c] = True

    labs.append(l)

coords = itertools.product(range(n), range(m))
coord_cases = itertools.combinations(coords, 3)
result = 0
for coord1, coord2, coord3 in coord_cases:
    if labs[coord1[0]][coord1[1]] != 0 or labs[coord2[0]][coord2[1]] != 0 or labs[coord3[0]][coord3[1]] != 0:
        continue

    tmp_labs = copy.deepcopy(labs)
    tmp_labs[coord1[0]][coord1[1]] = 1
    tmp_labs[coord2[0]][coord2[1]] = 1
    tmp_labs[coord3[0]][coord3[1]] = 1
    result = max(result, bfs(tmp_labs))

print(result)
