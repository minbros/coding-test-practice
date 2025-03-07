import sys

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))
dp1 = [1 for _ in range(n)]
dp2 = dp1.copy()
for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if seq[-(i + 1)] > seq[-(j + 1)]:
            dp2[-(i + 1)] = max(dp2[-(i + 1)], dp2[-(j + 1)] + 1)

result = []
for a, b in zip(dp1, dp2):
    result.append(a + b)

print(max(result) - 1)