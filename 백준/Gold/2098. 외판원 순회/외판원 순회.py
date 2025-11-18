import sys


def main():
    input = sys.stdin.readline
    INF = int(1e9)

    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * (1 << (n - 1)) for _ in range(n)]
    dp[0][0] = 0

    for visited in range(1 << (n - 1)):
        for cur_node in range(n):
            if dp[cur_node][visited] == INF:
                continue

            for next_node in range(1, n):
                bit_pos = 1 << (next_node - 1)
                if dist[cur_node][next_node] == 0 or visited & bit_pos:
                    continue

                new_visited = visited | bit_pos
                new_cost = dp[cur_node][visited] + dist[cur_node][next_node]
                dp[next_node][new_visited] = min(dp[next_node][new_visited], new_cost)

    full_mask = (1 << (n - 1)) - 1
    result = INF
    for node in range(n):
        if dp[node][full_mask] == INF or dist[node][0] == 0:
            continue
        result = min(result, dp[node][full_mask] + dist[node][0])

    print(result)


if __name__ == "__main__":
    main()
