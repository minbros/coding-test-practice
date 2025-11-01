from collections import deque

n, k = map(int, input().split())
answer = []
numbers = deque(range(1, n + 1))
while numbers:
    x = 0
    for _ in range(k - 1):
        x = numbers.popleft()
        numbers.append(x)
    x = numbers.popleft()
    answer.append(x)

print('<' + ', '.join(map(str, answer)) + '>')
