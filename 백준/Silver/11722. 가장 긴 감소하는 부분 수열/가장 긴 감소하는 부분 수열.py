import sys
import bisect

input = lambda: sys.stdin.readline()

n = int(input())
seq = list(map(int, input().split()))
lis = []    # lis[i]는 길이가 (i + 1)인 LIS(증가 부분 수열)을 만들기 위한 마지막 원소의 최솟값
for x in seq:
    i = bisect.bisect_left(lis, -x)
    if i >= len(lis):
        lis.append(-x)
    else:
        lis[i] = -x

print(len(lis))
