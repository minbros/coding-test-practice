import sys

input = lambda: sys.stdin.readline()


def solve():
    dp = [(0, 0, 0)] * n
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 3

    dp[0] = (1, 0, 0)
    dp[1] = (1, 1, 0)
    dp[2] = (1, 1, 1)
    for i in range(3, n):
        dp[i] = (dp[i - 1][0], dp[i - 2][0] + dp[i - 2][1], sum(dp[i - 3]))

    return sum(dp[-1])


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve())
