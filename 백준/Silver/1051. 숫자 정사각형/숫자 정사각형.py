import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = [input().rstrip() for _ in range(n)]
val = 1
for i in range(n - 1):
    for j in range(m - 1):
        for d in range(1, min(n - i, m - j)):
            if nums[i][j] == nums[i + d][j] == nums[i][j + d] == nums[i + d][j + d]:
                val = max(val, (d + 1) ** 2)

print(val)