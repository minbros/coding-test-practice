import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

INF = int(1e8)


def solve():
    queue = deque([(0, 0, 1)])
    dist = [[INF] * (m + 1) for _ in range(n + 1)]
    dist[1][0] = 0
    result = INF
    while queue:
        time, cost, now = queue.popleft()
        if now == n:
            result = min(result, time)
            continue

        if time > dist[now][cost]:
            continue

        for ti, co, to in graph[now]:
            new_cost = cost + co
            new_time = time + ti
            if new_cost > m or new_time >= dist[to][new_cost]:
                continue

            for i in range(new_cost + 1, m + 1):
                if dist[to][i] <= new_time:
                    break

                dist[to][i] = new_time

            dist[to][new_cost] = new_time
            queue.append((new_time, new_cost, to))

    return result


input()
n, m, k = map(int, input().split())
graph = defaultdict(list)

for _ in range(k):
    u, v, c, d = map(int, input().split())
    graph[u].append((d, c, v))
    
for key in graph.keys():
    graph[key].sort()

answer = solve()
print('Poor KCM' if answer == INF else answer)
