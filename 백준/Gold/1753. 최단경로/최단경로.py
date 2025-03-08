import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = float('inf')
m, n = map(int, input().split())
start = int(input().rstrip())
graph = defaultdict(list)
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []
heapq.heappush(q, (0, start))
distance = [INF] * (m + 1)
distance[start] = 0
while q:
    dist, frm = heapq.heappop(q)
    if distance[frm] < dist:
        continue

    for to, d in graph[frm]:
        if distance[to] > dist + d:
            distance[to] = dist + d
            heapq.heappush(q, (distance[to], to))

for i in range(1, m + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])