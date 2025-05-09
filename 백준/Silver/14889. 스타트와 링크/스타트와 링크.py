import sys
import itertools

input = sys.stdin.readline
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
players = list(range(1, n + 1))
cases = list(itertools.combinations(players, n // 2))
val = float('inf')
for team1 in cases[:len(cases) // 2]:
    team2 = tuple(x for x in players if x not in team1)
    stat1 = stat2 = 0
    for i, j in itertools.permutations(team1, 2):
        stat1 += table[i - 1][j - 1]
    for i, j in itertools.permutations(team2, 2):
        stat2 += table[i - 1][j - 1]

    val = min(val, abs(stat1 - stat2))

print(val)