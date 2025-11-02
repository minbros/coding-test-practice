import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
m = int(input())
dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]


def is_palindrome(start, end):
    stack = [(start, end)]
    while stack:
        s, e = stack[-1]
        if dp[s][e] != -1:
            stack.pop()
            continue

        if s >= e:
            dp[s][e] = 1
            stack.pop()
            continue

        if dp[s + 1][e - 1] != -1:
            if seq[s - 1] == seq[e - 1]:
                dp[s][e] = dp[s + 1][e - 1]
            else:
                dp[s][e] = 0
            stack.pop()
        else:
            stack.append((s + 1, e - 1))

    return dp[start][end]


result = []
for _ in range(m):
    s, e = map(int, input().split())
    result.append(str(is_palindrome(s, e)))
print('\n'.join(result))
