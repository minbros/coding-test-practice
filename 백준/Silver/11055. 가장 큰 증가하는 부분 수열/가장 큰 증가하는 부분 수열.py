import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = seq[i]
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + seq[i])

print(max(dp))