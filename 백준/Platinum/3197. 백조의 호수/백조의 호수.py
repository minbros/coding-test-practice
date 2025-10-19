from collections import deque

R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

swans = []
visited_swan = [[False for _ in range(C)] for _ in range(R)]

melted = set()
visited_water = [[False for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            melted.add((r, c))
            swans.append((r, c))
        elif lake[r][c] == '.':
            melted.add((r, c))
            visited_water[r][c] = True

x, y = swans[0]
visited_swan[x][y] = True


def melt():
    queue = deque(melted)
    new_melted = set()
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited_water[ni][nj] and lake[ni][nj] == 'X':
                new_melted.add((ni, nj))
                visited_water[ni][nj] = True

    return new_melted


def can_swans_meet(_start):
    queue = deque(_start)
    while queue:
        i, j = queue.popleft()
        if (i, j) == swans[1]:
            return True

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited_swan[ni][nj] and lake[ni][nj] != 'X':
                queue.append((ni, nj))
                visited_swan[ni][nj] = True

    return False


def p(matrix):
    for row in matrix:
        print(*row)

    print()


result = 0
start = {(x, y)}
while True:
    if can_swans_meet(start):
        print(result)
        quit()

    melted = melt()
    start = set()
    for r, c in melted:
        lake[r][c] = '.'
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and visited_swan[nr][nc]:
                start.add((r, c))
                visited_swan[r][c] = True
                break

    result += 1
