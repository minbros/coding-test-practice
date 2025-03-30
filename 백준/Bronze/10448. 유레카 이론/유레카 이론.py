import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
tri_nums = [n * (n + 1) // 2 for n in range(1, 45)]
sums = set(sum(c) for c in combinations_with_replacement(tri_nums, 3) if sum(c) <= 1000)
t = int(input())
for _ in range(t):
    k = int(input())
    print(int(k in sums))