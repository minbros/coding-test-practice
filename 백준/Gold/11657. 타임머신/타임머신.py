import sys

input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
costs = [INF for _ in range(n + 1)]
costs[1] = 0

succeeded = True
for i in range(n):
    for now, to, cost in roads:
        if costs[to] > costs[now] + cost:
            if i == n - 1:
                succeeded = False
                print(-1)
                break

            costs[to] = costs[now] + cost

if succeeded:
    for cost in costs[2:]:
        print(-1 if cost == INF else cost)
