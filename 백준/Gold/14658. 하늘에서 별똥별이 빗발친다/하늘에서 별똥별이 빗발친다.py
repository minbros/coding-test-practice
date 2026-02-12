import sys

input = lambda: sys.stdin.readline()


def count_stars(i1, i2, j1, j2):
    result = 0
    for i, j in stars:
        if i1 <= i <= i2 and j1 <= j <= j2:
            result += 1

    return result


n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]
answer = 0
for star1 in stars:
    x1 = star1[0]
    x2 = x1 + l
    for star2 in stars:
        y1 = star2[1]
        y2 = y1 + l
        answer = max(answer, count_stars(x1, x2, y1, y2))

print(k - answer)
