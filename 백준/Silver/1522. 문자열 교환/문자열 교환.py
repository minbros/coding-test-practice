import sys

input = lambda: sys.stdin.readline()

case = input().strip()
required = case.count('a')
result = 1000

for i in range(len(case)):
    j = (i + required) % len(case)
    if j < i:
        # 윈도우 밖에 있는 a의 개수 (윈도우가 쪼개져서 하나로 표현되지 않으니 간단하게 이렇게 표현)
        result = min(result, case[j:i].count('a'))
    else:
        # 윈도우 안에 있는 b의 개수
        result = min(result, case[i:j].count('b'))

print(result)
