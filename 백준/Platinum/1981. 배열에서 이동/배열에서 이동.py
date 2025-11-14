import sys
from collections import deque

input = sys.stdin.readline


def found_path(diff):
    for x in range(lower_bound, upper_bound - diff + 1):
        max_limit, min_limit = x + diff, x
        if not (min_limit <= grid[0][0] <= max_limit and min_limit <= grid[-1][-1] <= max_limit):
            continue

        if bfs(max_limit, min_limit):
            return True

    return False


def bfs(max_limit, min_limit):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, n - 1):
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and min_limit <= grid[nx][ny] <= max_limit:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return False


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
lower_bound, upper_bound = 200, 0
for row in grid:
    lower_bound = min(lower_bound, min(row))
    upper_bound = max(upper_bound, max(row))

left, right = 0, upper_bound - lower_bound
answer = 0
while left <= right:
    mid = (left + right) // 2
    if found_path(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
