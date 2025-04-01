import sys
import math
from itertools import combinations

input = sys.stdin.readline
cards = list(range(1, 11)) * 2
me = list(map(int, input().split()))
for c in me:
    cards.remove(c)

counts = 0
if me[0] == me[1]:
    for comb in combinations(cards, 2):
        if comb[0] != comb[1] or me[0] > comb[0]:
            counts += 1
else:
    for comb in combinations(cards, 2):
        if comb[0] != comb[1] and sum(me) % 10 > sum(comb) % 10:
            counts += 1

print(f"{counts / math.comb(18 , 2):.3f}")