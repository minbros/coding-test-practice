import sys
from collections import deque

input = lambda: sys.stdin.readline()

LIMIT = 140_000

n, k = map(int, input().split())
visited = [False] * (LIMIT + 1)
queue = deque([(n, 0)])
while queue:
    x, d = queue.popleft()
    while x < LIMIT and not visited[x]:
        if x == k:
            print(d)
            quit(0)

        visited[x] = True
        if x > 0 and not visited[x - 1]:
            queue.append((x - 1, d + 1))
        if not visited[x + 1]:
            queue.append((x + 1, d + 1))

        x <<= 1
