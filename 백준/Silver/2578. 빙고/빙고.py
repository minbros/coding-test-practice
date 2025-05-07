import sys

diagonal1 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
diagonal2 = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]


def check_lines(row, col):
    result = 0
    if (row, col) in diagonal1:
        correct = True
        for x, y in diagonal1:
            if board[x][y] != 0:
                correct = False
                break

        if correct:
            result += 1

    if (row, col) in diagonal2:
        correct = True
        for x, y in diagonal2:
            if board[x][y] != 0:
                correct = False
                break

        if correct:
            result += 1

    if board[row][0] == board[row][1] == board[row][2] == board[row][3] == board[row][4] == 0:
        result += 1

    if board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == 0:
        result += 1

    return result


input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(5)]
host = sum([list(map(int, input().split())) for _ in range(5)], [])
lines = 0
for i, n in enumerate(host):
    found = False
    for r in range(5):
        for c in range(5):
            if board[r][c] == n:
                board[r][c] = 0
                lines += check_lines(r, c)
                found = True
                break

        if found:
            break

    if lines >= 3:
        print(i + 1)
        break
