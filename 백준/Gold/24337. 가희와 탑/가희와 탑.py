import sys

input = lambda: sys.stdin.readline()

n, a, b = map(int, input().split())
answer = None
if a + b >= n + 2:
    answer = [-1]
else:
    k = n - (a + b)
    if a >= b:
        answer = [1] * (k + 1) + list(range(1, a + 1)) + list(range(b - 1, 0, -1))
    else:
        if a == 1:
            answer = [b] + [1] * (k + 1) + list(range(b - 1, 0, -1))
        else:
            answer = [1] * (k + 1) + list(range(1, a)) + list(range(b, 0, -1))

print(*answer)
