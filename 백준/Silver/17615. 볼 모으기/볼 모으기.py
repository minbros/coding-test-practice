import sys

input = lambda: sys.stdin.readline()

n = int(input())
balls = input().strip()
left = 0
while left < n - 1 and balls[left + 1] == balls[0]:
    left += 1

right = n - 1
while right > 0 and balls[right - 1] == balls[n - 1]:
    right -= 1

if balls[0] == balls[n - 1]:
    if left + 1 > n - right:
        cmp = balls[left + 1:]
    else:
        cmp = balls[:right]
else:
    cmp = balls[left + 1: right]

count = cmp.count('R')
print(min(count, len(cmp) - count))
