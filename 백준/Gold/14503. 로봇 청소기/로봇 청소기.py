import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
empty_count = sum([row.count(0) for row in grid])
result = 0


def is_empty_around(_r, _c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for d1, d2 in zip(dr, dc):
        nr = _r + d1
        nc = _c + d2
        if n > nr >= 0 == grid[nr][nc] and 0 <= nc < m:
            return True

    return False


while result < empty_count:
    if grid[r][c] == 0:
        result += 1
        grid[r][c] = -1

    if is_empty_around(r, c):
        for _ in range(4):
            d = (d - 1) % 4
            if d == 0 and grid[r - 1][c] == 0:
                r -= 1
                break

            elif d == 1 and grid[r][c + 1] == 0:
                c += 1
                break

            elif d == 2 and grid[r + 1][c] == 0:
                r += 1
                break

            elif d == 3 and grid[r][c - 1] == 0:
                c -= 1
                break

    else:
        cmp_r = r
        cmp_c = c
        if d == 0 and grid[r + 1][c] != 1:
            cmp_r = r + 1

        elif d == 1 and grid[r][c - 1] != 1:
            cmp_c = c - 1

        elif d == 2 and grid[r - 1][c] != 1:
            cmp_r = r - 1

        elif d == 3 and grid[r][c + 1] != 1:
            cmp_c = c + 1

        if cmp_r == r and cmp_c == c:
            break

        r = cmp_r
        c = cmp_c

print(result)
