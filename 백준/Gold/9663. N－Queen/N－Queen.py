n = int(input())
queens = [0] * n
result = 0


def is_safe(row):
    for i in range(row):
        if queens[row] == queens[i]:
            return False

        if abs(i - row) == abs(queens[i] - queens[row]):
            return False

    return True


def find(row):
    global result
    if row == n:
        result += 1
        return

    for col in range(n):
        queens[row] = col
        if is_safe(row):
            find(row + 1)


find(0)
print(result)
