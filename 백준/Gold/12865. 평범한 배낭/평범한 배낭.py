import sys

input = sys.stdin.readline

n, k = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(k + 1):
        if weights[i - 1] > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

print(dp[n][k])
