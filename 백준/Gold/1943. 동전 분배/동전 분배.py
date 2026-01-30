import sys

input = lambda: sys.stdin.readline()


def solve():
    dp = [False] * (target + 1)
    dp[0] = True
    for _amount, _count in coins:
        for i in range(target, _amount - 1, -1):
            if not dp[i - _amount]:
                continue

            k = i
            iteration = 0
            while k <= target and iteration < _count:
                dp[k] = True
                k += _amount
                iteration += 1

        if dp[-1]:
            return True

    return dp[-1]


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
