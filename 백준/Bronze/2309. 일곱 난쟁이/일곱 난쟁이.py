import sys
from itertools import combinations

input = sys.stdin.readline
nums = [int(input()) for _ in range(9)]

for combination in combinations(nums, 7):
    if sum(combination) == 100:
        for n in sorted(combination):
            print(n)
        break