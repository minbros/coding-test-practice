import sys

input = lambda: sys.stdin.readline()


def main():
    n = int(input())
    costs = [tuple(map(int, input().split())) for _ in range(n)]
    result = float('inf')

    for start in range(3):
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][start] = costs[0][start]

        for i in range(1, n - 1):
            for j in range(3):
                a, b = (j + 1) % 3, (j + 2) % 3
                dp[i][j] = min(dp[i - 1][a], dp[i - 1][b]) + costs[i][j]

        for end in range(3):
            if start == end:
                continue

            a, b = (end + 1) % 3, (end + 2) % 3
            dp[-1][end] = min(dp[-2][a], dp[-2][b]) + costs[-1][end]

        result = min(result, min(dp[-1]))

    print(result)


if __name__ == "__main__":
    main()
