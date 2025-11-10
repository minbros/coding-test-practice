import sys

input = sys.stdin.readline

n = int(input())
mat_list = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(i, n):
        for k in range(j - i, j):
            r, x, c = mat_list[j - i][0], mat_list[k][1], mat_list[j][1]
            cmp = dp[j - i][k] + r * x * c + dp[k + 1][j]

            if dp[j - i][j] == 0 or dp[j - i][j] > cmp:
                dp[j - i][j] = cmp

print(dp[0][-1])
