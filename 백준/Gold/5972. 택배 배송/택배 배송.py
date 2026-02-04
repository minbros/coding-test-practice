import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline()
INF = 1e8

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

costs = [INF] * (n + 1)
costs[1] = 0
heap = [(0, 1)]
while heap:
    dist, cur = heapq.heappop(heap)
    if costs[cur] < dist:
        continue

    if cur == n:
        print(costs[n])
        break

    for more, end in graph[cur]:
        new_cost = dist + more
        if costs[end] > new_cost:
            costs[end] = new_cost
            heapq.heappush(heap, (new_cost, end))
