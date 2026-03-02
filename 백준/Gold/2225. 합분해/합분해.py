import sys
import math

input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
print(math.comb(n + k - 1, n) % int(1e9))
