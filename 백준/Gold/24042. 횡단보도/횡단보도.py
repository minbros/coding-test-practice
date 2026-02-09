import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline()
INF = float('inf')


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, i))
        graph[b].append((a, i))

    heap = [(0, 1)]
    dist = [INF] * (n + 1)
    dist[1] = 0
    while heap:
        time, cur = heapq.heappop(heap)
        if dist[cur] < time:
            continue

        for end, idx in graph[cur]:
            waiting = (idx - time % m + m) % m
            new_time = time + waiting + 1
            if dist[end] > new_time:
                dist[end] = new_time
                heapq.heappush(heap, (new_time, end))

    print(dist[-1])


if __name__ == '__main__':
    main()
