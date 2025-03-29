import sys

input = sys.stdin.readline
n = int(input())

for cmp in range(1, n + 1):
    if cmp + sum(map(int, list(str(cmp)))) == n:
        print(cmp)
        quit()

print(0)