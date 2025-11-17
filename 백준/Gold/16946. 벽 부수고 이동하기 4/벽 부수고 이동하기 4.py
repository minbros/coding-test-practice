import sys
from collections import deque

input = lambda: sys.stdin.readline()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def change_grid():
    clusters = get_clusters()

    coord_to_cluster = {}
    for index, cluster in enumerate(clusters):
        for coord in cluster:
            coord_to_cluster[coord] = index

    for i, j in walls:
        visited = set()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (ni, nj) not in coord_to_cluster:
                continue

            index = coord_to_cluster[(ni, nj)]
            if index in visited:
                continue

            grid[i][j] = (grid[i][j] + len(clusters[index])) % 10
            visited.add(index)


def get_clusters():
    visited = [[False] * m for _ in range(n)]
    clusters = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] or grid[i][j] != 0:
                continue

            queue = deque([(i, j)])
            visited[i][j] = True
            cluster = {(i, j)}
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        cluster.add((nx, ny))

            clusters.append(cluster)

    return clusters


n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
walls = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

change_grid()

for row in grid:
    print(''.join(map(str, row)))
