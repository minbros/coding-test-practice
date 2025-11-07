import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = sum(costs)
dp = [[0 for _ in range(total_cost + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(total_cost + 1):
        if j < costs[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + memories[i - 1])

for cost, memory in enumerate(dp[n]):
    if memory >= m:
        print(cost)
        break
