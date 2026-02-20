import sys
import bisect

input = lambda: sys.stdin.readline()

n = int(input())
kids = [int(input()) for _ in range(n)]
lis = []    # lis[i]는 길이가 (i + 1)인 LIS(증가 부분 수열)을 만들기 위한 마지막 원소의 최솟값
for k in kids:
    i = bisect.bisect_left(lis, k)
    if i >= len(lis):
        lis.append(k)
    else:
        lis[i] = k

print(n - len(lis))
