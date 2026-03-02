import sys

input = lambda: sys.stdin.readline()
INF = int(1e8)

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
dp = [0] + [INF] * k

for i in range(1, k + 1):
    for v in values:
        if i - v < 0:
            continue
            
        dp[i] = min(dp[i], dp[i - v] + 1)

print(dp[-1] if dp[-1] < INF else -1)
