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
start = {(x, y)}
visited_swan[x][y] = True


def melt():
    global melted
    queue = deque(melted)
    melted = set()
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited_water[ni][nj] and lake[ni][nj] == 'X':
                melted.add((ni, nj))
                visited_water[ni][nj] = True


def can_swans_meet():
    global start
    queue = deque(start)
    start = set()
    while queue:
        i, j = queue.popleft()
        if (i, j) == swans[1]:
            return True

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited_swan[ni][nj]:
                visited_swan[ni][nj] = True
                if lake[ni][nj] == 'X':
                    start.add((ni, nj))
                else:
                    queue.append((ni, nj))

    return False


result = 0
while True:
    if can_swans_meet():
        print(result)
        quit()

    melt()
    for r, c in melted:
        lake[r][c] = '.'

    result += 1
