# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def dfs(n, i, numbers, target):
    if i > len(numbers) - 1:
        if n == target:
            return 1
        else:
            return 0
    else:
        return dfs(n + numbers[i], i + 1, numbers, target) + dfs(n - numbers[i], i + 1, numbers, target)


def solution(numbers, target):
    return dfs(0, 0, numbers, target)
