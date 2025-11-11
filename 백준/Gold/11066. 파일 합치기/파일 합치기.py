import sys

input = sys.stdin.readline


def solve(a, b):
    if dp[a][b] != -1:
        return dp[a][b]

    if a == b:
        return 0

    result = float('inf')
    val = sums[b + 1] - sums[a]
    for x in range(a, b):
        result = min(result, solve(a, x) + solve(x + 1, b) + val)

    dp[a][b] = result
    return result


t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[-1 for _ in range(k)] for _ in range(k)]
    sums = [0] * (k + 1)
    for i in range(1, k + 1):
        sums[i] = sums[i - 1] + files[i - 1]

    print(solve(0, k - 1))
