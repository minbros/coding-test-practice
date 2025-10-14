import sys

input = sys.stdin.readline

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
result = 0


def get_value(_grid):
    value = 0
    for row in _grid:
        i = 0
        cmp = row[0]
        while True:
            streak = 0
            while i < N and row[i] == cmp:
                streak += 1
                i += 1

            if i >= N:
                value += 1
                break

            if abs(cmp - row[i]) > 1:
                break

            if cmp < row[i]:
                if streak < L:
                    break
                else:
                    cmp = row[i]
            else:
                streak = 0
                cmp = row[i]
                while i < N and row[i] == cmp and streak < L:
                    streak += 1
                    i += 1

                if streak < L:
                    break
                else:
                    cmp = row[i - 1]

    return value


print(get_value(grid) + get_value(zip(*grid)))
