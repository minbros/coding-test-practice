import sys

input = lambda: sys.stdin.readline()


def solve(diag, idx, cur, other_diag_allowed):
    global result
    if idx == len(diag):
        result = max(result, cur)
        return

    for x, y in diag[idx]:
        k = x - y + n - 1
        cmp = 1 << (k // 2)
        if other_diag_allowed & cmp:
            solve(diag, idx + 1, cur + 1, other_diag_allowed & ~cmp)        

    solve(diag, idx + 1, cur, other_diag_allowed)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
white_diag = [[] for _ in range(n)]
black_diag = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] != 1:
            continue
        
        if (i + j) % 2 == 0:
            white_diag[(i + j) // 2].append((i, j))
        else:
            black_diag[(i + j) // 2].append((i, j))
            
result = 0
solve(white_diag, 0, 0, (1 << n) - 1)

answer = result
result = 0
solve(black_diag, 0, 0, (1 << n) - 1)

answer += result
print(answer)
