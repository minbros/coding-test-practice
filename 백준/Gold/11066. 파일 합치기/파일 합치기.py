import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]
    a = [[0 for _ in range(k)] for _ in range(k)]
    sums = [0] * (k + 1)

    for i in range(1, k + 1):
        sums[i] = sums[i - 1] + files[i - 1]

    for L in range(2, k + 1):
        for i in range(k - L + 1):
            j = i + L - 1
            preset = sums[j + 1] - sums[i]
            start = a[i][j - 1] if a[i][j - 1] else i
            end = a[i + 1][j] if a[i + 1][j] else j - 1
            for x in range(start, end + 1):
                val = dp[i][x] + dp[x + 1][j] + preset
                if dp[i][j] > val or dp[i][j] == 0:
                    dp[i][j] = val
                    a[i][j] = x

    print(dp[0][-1])
