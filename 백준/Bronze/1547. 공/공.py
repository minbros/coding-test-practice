import sys

input = sys.stdin.readline
cups = [0, 1, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    tmp = cups[a]
    cups[a] = cups[b]
    cups[b] = tmp

if 1 in cups:
    print(cups.index(1))
else:
    print(-1)