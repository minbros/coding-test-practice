import sys
from functools import cmp_to_key


def compare(a, b):
    if a + b >= b + a:
        return -1
    else:
        return 1


_input = sys.stdin.readline
n = int(_input())
numbers = list(map(str, _input().split()))
print(int(''.join(sorted(numbers, key=cmp_to_key(compare)))))
