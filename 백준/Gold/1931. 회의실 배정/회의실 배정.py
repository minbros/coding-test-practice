import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

t = 0
result = 0
meetings.sort(key=lambda x: (x[1], x[0]))
for start, end in meetings:
    if start >= t:
        result += 1
        t = end

print(result)
