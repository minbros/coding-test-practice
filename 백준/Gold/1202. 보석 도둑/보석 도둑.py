import sys
import heapq

input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
heapq.heapify(jewels)
bags = sorted([int(input()) for _ in range(k)])

result = 0
possible = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(possible, (-v, m))

    if possible:
        result -= heapq.heappop(possible)[0]

print(result)
