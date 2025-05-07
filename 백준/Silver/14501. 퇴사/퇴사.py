import sys

input = sys.stdin.readline
T_i = []
P_i = []
n = int(input())
for _ in range(n):
    t, p = map(int, input().split())
    T_i.append(t)
    P_i.append(p)

dp = [0 for _ in range(n + 1)]
for i in range(n):
    dp[i + 1] = max(dp[i], dp[i + 1])
    if i + T_i[i] < n + 1:
        dp[i + T_i[i]] = max(dp[i + T_i[i]], dp[i] + P_i[i])

print(dp[-1])
