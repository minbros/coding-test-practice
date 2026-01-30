import sys

input = lambda: sys.stdin.readline()


def solve():
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        _amount, _count = coins[i - 1]
        for j in range(target + 1):
            if not dp[i - 1][j]:
                continue

            k = j
            iteration = 0
            while k <= target and iteration <= _count:
                dp[i][k] = True
                k += _amount
                iteration += 1

    return dp[-1][-1]


for _ in range(3):
    n = int(input())
    coins = []
    target = 0
    for _ in range(n):
        amount, count = map(int, input().split())
        coins.append((amount, count))
        target += amount * count

    if target % 2 == 0:
        target //= 2
        print(int(solve()))
    else:
        print(0)
