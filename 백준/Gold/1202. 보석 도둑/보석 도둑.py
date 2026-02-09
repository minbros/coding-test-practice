import sys
import heapq

input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
jewels = sorted([tuple(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])

idx = 0
result = 0
possible = []
for bag in bags:
    while idx < n and jewels[idx][0] <= bag:
        m, v = jewels[idx]
        heapq.heappush(possible, (-v, m))
        idx += 1

    if possible:
        result -= heapq.heappop(possible)[0]

print(result)
