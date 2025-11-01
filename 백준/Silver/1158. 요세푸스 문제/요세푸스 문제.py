n, k = map(int, input().split())
answer = []
numbers = list(range(1, n + 1))
cur = 0
while numbers:
    cur = (cur + k - 1) % len(numbers)
    answer.append(numbers.pop(cur))

print('<' + ', '.join(map(str, answer)) + '>')
