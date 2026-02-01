import sys
import heapq

input = lambda: sys.stdin.readline()
INF = 1e8

n, m, x = map(int, input().split())
graph1 = [[INF] * (n + 1) for _ in range(n + 1)]  # 정방향 그래프
graph2 = [[INF] * (n + 1) for _ in range(n + 1)]  # 역방향 그래프
for _ in range(m):
    a, b, t = map(int, input().split())
    graph1[a][b] = t
    graph2[b][a] = t


def dijkstra(graph):
    heap = [(0, x)]
    dist = [0] + [INF] * n
    dist[x] = 0
    while heap:
        time, cur = heapq.heappop(heap)
        if dist[cur] < time:
            continue

        for end, new_time in enumerate(graph[cur]):
            if dist[end] > time + new_time:
                dist[end] = time + new_time
                heapq.heappush(heap, (time + new_time, end))

    return dist


result = 0
dist1 = dijkstra(graph1)
dist2 = dijkstra(graph2)
for i in range(1, n + 1):
    result = max(result, dist1[i] + dist2[i])

print(result)
