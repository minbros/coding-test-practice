import sys

input = lambda: sys.stdin.readline()


def find_parent(x):
    if parents[x] == x:
        return x
    return find_parent(parents[x])


n = int(input())
m = int(input())
connected = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parents = list(range(n))

for i in range(n):
    for j in range(i + 1, n):
        if not connected[i][j]:
            continue

        i_parent = find_parent(i)
        j_parent = find_parent(j)
        if i_parent != j_parent:
            parents[j_parent] = i_parent

plan_parents = set(find_parent(p - 1) for p in plan)
print('YES' if len(plan_parents) == 1 else 'NO')
