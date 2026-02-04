import sys

input = lambda: sys.stdin.readline()
INF = int(1e8)

n = int(input())
heights = list(map(int, input().split()))

stack = []
counts = [0] * n
closest_numbers = [INF] * n
for i in range(n - 2, -1, -1):
    if heights[i] < heights[i + 1]:
        stack.append((heights[i + 1], i + 1))
    else:
        while stack:
            h, k = stack[-1]
            if heights[i] < h:
                break

            stack.pop()

    counts[i] += len(stack)
    if stack:
        closest = stack[-1][1]
        if abs(closest - i) < abs(i - closest_numbers[i] + 1):
            closest_numbers[i] = closest + 1

stack = []
for i in range(1, n):
    if heights[i] < heights[i - 1]:
        stack.append((heights[i - 1], i - 1))
    else:
        while stack:
            h, k = stack[-1]
            if heights[i] < h:
                break

            stack.pop()

    counts[i] += len(stack)
    if stack:
        closest = stack[-1][1]
        if abs(closest - i) <= abs(i - closest_numbers[i] + 1):
            closest_numbers[i] = closest + 1

for ans1, ans2 in zip(counts, closest_numbers):
    if ans1 == 0:
        print(0)
    else:
        print(ans1, ans2)
