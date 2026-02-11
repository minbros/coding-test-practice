import sys

input = lambda: sys.stdin.readline()

n = int(input())
towers = list(map(int, input().split()))
result = [0] * n

stack = []
for i, h in enumerate(towers):
    while stack and stack[-1][1] <= h:
        stack.pop()

    if stack:
        result[i] = stack[-1][0]

    stack.append((i + 1, h))

print(*result)
