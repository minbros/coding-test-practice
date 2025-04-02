import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
cmp1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
cmp2 = ['BWBWBWBW', 'WBWBWBWB'] * 4
val = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        chess = [board[k][j: j + 8] for k in range(i, i + 8)]
        count1 = 0
        count2 = 0
        for r in range(8):
            for c in range(8):
                if chess[r][c] != cmp1[r][c]:
                    count1 += 1
                if chess[r][c] != cmp2[r][c]:
                    count2 += 1

        val = min(val, count1, count2)

print(val)
