import sys

input = lambda: sys.stdin.readline()

t = int(input())
inputs = [int(input()) for _ in range(t)]
m = max(inputs)
dp = [1] + [0] * m
for k in (1, 2, 3):
    for i in range(k, m + 1):
        dp[i] += dp[i - k]

for i in inputs:
    print(dp[i])
