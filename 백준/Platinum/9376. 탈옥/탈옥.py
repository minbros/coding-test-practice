import sys
from collections import deque

input = sys.stdin.readline


def bfs(coord):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[-1 for _ in range(w + 2)] for _ in range(h + 2)]
    x, y = coord
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h + 2 and 0 <= nc < w + 2 and visited[nr][nc] == -1:
                if grid[nr][nc] in ('.', '$'):
                    queue.appendleft((nr, nc))
                    visited[nr][nc] = visited[r][c]
                elif grid[nr][nc] == '#':
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    return visited


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = ['.' * (w + 2)] + ['.' + input().strip() + '.' for _ in range(h)] + ['.' * (w + 2)]
    prisoners = [(r, c) for r in range(h + 2) for c in range(w + 2) if grid[r][c] == '$']

    visited1 = bfs(prisoners[0])
    visited2 = bfs(prisoners[1])
    visited_outside = bfs((0, 0))

    result = float('inf')
    for i in range(h + 2):
        for j in range(w + 2):
            if visited1[i][j] == -1 or visited2[i][j] == -1 or visited_outside[i][j] == -1:
                continue

            total = visited1[i][j] + visited2[i][j] + visited_outside[i][j]
            if grid[i][j] == '#':
                total -= 2

            result = min(result, total)

    print(result)
