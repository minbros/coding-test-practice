import sys

input = lambda: sys.stdin.readline()
INF = int(1e8)


def clear_stack():
    while stack:
        if heights[i] < stack[-1][0]:
            break

        stack.pop()


def renew_closest_number():
    if stack:
        closest = stack[-1][1]
        if abs(closest - i) <= abs(i - closest_numbers[i] + 1):
            closest_numbers[i] = closest + 1


n = int(input())
heights = list(map(int, input().split()))

stack = []
counts = [0] * n
closest_numbers = [INF] * n
for i in range(n - 2, -1, -1):
    if heights[i] < heights[i + 1]:
        stack.append((heights[i + 1], i + 1))
    else:
        clear_stack()

    counts[i] += len(stack)
    renew_closest_number()

stack = []
for i in range(1, n):
    if heights[i] < heights[i - 1]:
        stack.append((heights[i - 1], i - 1))
    else:
        clear_stack()

    counts[i] += len(stack)
    renew_closest_number()

for ans1, ans2 in zip(counts, closest_numbers):
    if ans1 == 0:
        print(0)
    else:
        print(ans1, ans2)
