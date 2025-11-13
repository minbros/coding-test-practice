import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def found_path(start, end, arr):
    return {start, end} == {g, h} or arr[start]  # 찾아낸 경로로 향하거나, 이미 찾아낸 경로를 지나감


def dijkstra():
    heap = [(0, s)]
    costs = [float('inf')] * (n + 1)
    costs[s] = 0
    result = [False] * (n + 1)  # g-h 도로 사용 여부

    while heap:
        dist, now = heapq.heappop(heap)
        if costs[now] < dist:
            continue

        for to, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < costs[to]:
                costs[to] = new_cost
                result[to] = found_path(now, to, result)
                heapq.heappush(heap, (costs[to], to))

            elif new_cost == costs[to] and not result[to]:
                result[to] = found_path(now, to, result)

    return result


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    candidates = [int(input()) for _ in range(t)]
    passed = dijkstra()
    answer = [node for node in sorted(candidates) if passed[node]]
    print(*answer)
