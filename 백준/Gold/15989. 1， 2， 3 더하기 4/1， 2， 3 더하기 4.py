import sys

input = lambda: sys.stdin.readline()


def solve():
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in (1, 2, 3):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]

    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve())
