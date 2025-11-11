import sys

input = sys.stdin.readline


def max_area(arr):
    stack = []
    result = 0
    for i, h in enumerate(arr):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            result = max(result, height * (i - index))
            start = index
        stack.append((start, h))

    for index, height in stack:
        result = max(result, height * (len(arr) - index))

    return result


while True:
    n, *heights = map(int, input().split())
    if n == 0: break
    print(max_area(heights))
