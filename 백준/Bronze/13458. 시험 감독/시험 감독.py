import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0

for i in range(n):
    tmp = a[i]
    tmp -= b
    result += 1

    if tmp <= 0:
        continue

    result += tmp // c
    if tmp % c != 0:
        result += 1

print(result)