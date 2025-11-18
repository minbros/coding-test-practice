import sys

input = lambda: sys.stdin.readline()

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * n for _ in range(1 << (n - 1))]
dp[0][0] = 0

for visited in range(1 << (n - 1)):
    for cur_node in range(n):
        if dp[visited][cur_node] == float('inf'):
            continue

        for next_node in range(1, n):
            bit_pos = 1 << (next_node - 1)
            if dist[cur_node][next_node] == 0 or visited & bit_pos:
                continue

            new_visited = visited | bit_pos
            new_cost = dp[visited][cur_node] + dist[cur_node][next_node]
            dp[new_visited][next_node] = min(dp[new_visited][next_node], new_cost)

result = float('inf')
for node, cost in enumerate(dp[-1]):
    if dist[node][0] == 0:
        continue

    result = min(result, cost + dist[node][0])

print(result)
