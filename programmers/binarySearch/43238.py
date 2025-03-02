# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    k = min(times)
    left = k
    right = k * n
    result = 0
    while left <= right:
        middle = (left + right) // 2
        tmp = [middle // t for t in times]
        if sum(tmp) >= n:
            result = middle
            right = middle - 1
        else:
            left = middle + 1

    return result
