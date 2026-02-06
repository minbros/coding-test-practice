import sys

input = lambda: sys.stdin.readline()
INF = float('inf')

min_candidates = {
    2: 1,
    3: 7,
    4: 4,
    5: 2,
    6: 0,
    7: 8
}


def get_max_answer(n):
    if n % 2 == 0:
        return '1' * (n // 2)

    return '7' + '1' * (n // 2 - 1)


t = int(input())
inputs = [int(input()) for _ in range(t)]
m = max(inputs)

dp = [INF] * (m + 1)
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8

for i in range(8, m + 1):
    if i % 7 == 0:
        dp[i] = int('8' * (i // 7))
        continue

    for key, val in min_candidates.items():
        k = i - key
        if dp[k] == INF:
            continue

        cur = str(dp[k])
        if val == 0:
            cmp = cur[0] + '0' + cur[1:]
        else:
            zero_count = cur.count('0')
            if val < int(cur[0]):
                cmp = str(val) + cur[1: zero_count + 1] + cur[0] + cur[zero_count + 1:]
            else:
                cmp = cur[:zero_count + 1] + ''.join(sorted(cur[zero_count + 1:] + str(val)))

        dp[i] = min(dp[i], int(cmp))

for num in inputs:
    print(dp[num], get_max_answer(num))
