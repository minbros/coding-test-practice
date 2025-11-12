import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline


def solve():
    distance = defaultdict(list)
    nodes = [robot] + dirts
    for x in range(len(nodes)):
        for y in range(x + 1, len(nodes)):
            start, end = nodes[x], nodes[y]
            val = bfs(start, end)
            if val is not None:
                distance[x].append((y, val))
                distance[y].append((x, val))

    dp = [[float('inf') for _ in range(len(nodes))] for _ in range(1 << len(nodes))]
    dp[1][0] = 0

    for visited in range(1, 1 << len(nodes)):
        for cur_node in range(len(nodes)):
            if dp[visited][cur_node] == float('inf'):
                continue
            if not (visited & (1 << cur_node)):
                continue

            for next_node, cost in distance[cur_node]:
                if visited & (1 << next_node):
                    continue

                new_visited = visited | (1 << next_node)
                dp[new_visited][next_node] = min(dp[new_visited][next_node], dp[visited][cur_node] + cost)

    result = float('inf')
    all_visited = (1 << len(nodes)) - 1
    for x in range(1, len(nodes)):
        result = min(result, dp[all_visited][x])

    return -1 if result == float('inf') else result


def bfs(start, end):
    visited = [[False for _ in range(w)] for _ in range(h)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start[0], start[1], 0)])
    while queue:
        x, y, d = queue.popleft()
        if (x, y) == end:
            return d

        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 'x' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, d + 1))

    return None


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    grid = [input().strip() for _ in range(h)]
    dirts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'o':
                robot = (i, j)
            elif grid[i][j] == '*':
                dirts.append((i, j))

    print(solve())
