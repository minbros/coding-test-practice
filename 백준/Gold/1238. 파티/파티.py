import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline()
INF = 1e8


def dijkstra(graph, start):
    heap = [(0, start)]
    dist = [0] + [INF] * n
    dist[start] = 0
    while heap:
        time, cur = heapq.heappop(heap)
        if dist[cur] < time:
            continue

        for new_time, end in graph[cur]:
            if dist[end] > time + new_time:
                dist[end] = time + new_time
                heapq.heappush(heap, (time + new_time, end))

    return dist


n, m, x = map(int, input().split())
graph1 = defaultdict(list)  # 정방향 그래프
graph2 = defaultdict(list)  # 역방향 그래프
for _ in range(m):
    a, b, t = map(int, input().split())
    graph1[a].append((t, b))
    graph2[b].append((t, a))

result = 0
dist1 = dijkstra(graph1, x)
dist2 = dijkstra(graph2, x)
for i in range(1, n + 1):
    result = max(result, dist1[i] + dist2[i])

print(result)
