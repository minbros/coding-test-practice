import sys
from itertools import combinations


def solve(_chicken_coords):
    value = 0
    for house in house_coords:
        tmp = float('inf')
        for chicken in _chicken_coords:
            tmp = min(tmp, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))

        value += tmp

    result.add(value)


_input = sys.stdin.readline
n, m = map(int, _input().split())
table = []
house_coords = []
chicken_coords = []
for _ in range(n):
    table.append(list(map(int, _input().split())))

for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            house_coords.append((i, j))
        elif table[i][j] == 2:
            chicken_coords.append((i, j))

result = set()
for case in combinations(chicken_coords, m):
    solve(case)

print(min(result))