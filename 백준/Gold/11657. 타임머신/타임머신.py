import sys

input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
costs = [INF for _ in range(n + 1)]
costs[1] = 0

for i in range(n - 1):
    for now, to, cost in roads:
        if costs[to] > costs[now] + cost:
            costs[to] = costs[now] + cost
            
succeeded = True
for now, to, cost in roads:
    if costs[to] > costs[now] + cost:
        succeeded = False
        print(-1)
        break

if succeeded:
    result = [-1 if cost == INF else cost for cost in costs[2:]]
    print('\n'.join(map(str, result)))
