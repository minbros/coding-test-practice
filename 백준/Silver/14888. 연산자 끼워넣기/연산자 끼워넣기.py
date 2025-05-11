import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
symbols = list(map(int, input().split()))
INF = float('inf')
results = [-INF, INF]


def solve(val, depth):
    if depth == len(numbers) - 1:
        results[0] = max(results[0], val)
        results[1] = min(results[1], val)
        return

    if symbols[0] != 0:
        symbols[0] -= 1
        solve(val + numbers[depth + 1], depth + 1)
        symbols[0] += 1

    if symbols[1] != 0:
        symbols[1] -= 1
        solve(val - numbers[depth + 1], depth + 1)
        symbols[1] += 1

    if symbols[2] != 0:
        symbols[2] -= 1
        solve(val * numbers[depth + 1], depth + 1)
        symbols[2] += 1

    if symbols[3] != 0:
        symbols[3] -= 1
        solve(int(val / numbers[depth + 1]), depth + 1)
        symbols[3] += 1


solve(numbers[0], 0)
print(results[0], results[1], sep='\n')
