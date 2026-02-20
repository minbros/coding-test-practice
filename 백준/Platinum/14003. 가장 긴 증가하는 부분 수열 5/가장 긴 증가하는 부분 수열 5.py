import sys
import bisect

input = lambda: sys.stdin.readline()

n = int(input())
seq = list(map(int, input().split()))
lis = []
parent = [0] * n
for i, x in enumerate(seq):
    idx = bisect.bisect_left(lis, x)
    if idx >= len(lis):
        lis.append(x)
    else:
        lis[idx] = x

    parent[i] = idx

print(len(lis))
answer = []
k = len(lis) - 1
for i in range(n - 1, -1, -1):
    if parent[i] == k:
        answer.append(seq[i])
        k -= 1

print(*answer[::-1])
