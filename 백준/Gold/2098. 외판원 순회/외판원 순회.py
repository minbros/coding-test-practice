import sys

input = lambda: sys.stdin.readline()

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[(0, float('inf'))] * n for _ in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = (1 << i, 0)

for visited in range(1, 1 << n):
    for cur_node in range(n):
        if dp[visited][cur_node][1] == float('inf'):
            continue

        if not (visited & (1 << cur_node)):
            continue

        for next_node in range(n):
            if dist[cur_node][next_node] == 0 or visited & (1 << next_node):
                continue

            new_visited = visited | (1 << next_node)
            new_cost = dp[visited][cur_node][1] + dist[cur_node][next_node]
            if new_cost < dp[new_visited][next_node][1]:
                dp[new_visited][next_node] = (dp[visited][cur_node][0], new_cost)

            elif new_cost == dp[new_visited][next_node][1]:
                start_nodes = dp[visited][cur_node][0] | dp[new_visited][next_node][0]
                dp[new_visited][next_node] = (start_nodes, new_cost)

result = float('inf')
for cur_node, (next_nodes, cost) in enumerate(dp[-1]):
    for next_node in range(n):
        if not (next_nodes & (1 << next_node)) or dist[cur_node][next_node] == 0:
            continue

        result = min(result, cost + dist[cur_node][next_node])

print(result)
