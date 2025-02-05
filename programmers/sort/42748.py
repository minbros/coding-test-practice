# K번째 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    result = []

    for command in commands:
        i, j, k = command
        new = sorted(array[i - 1: j])[k - 1]
        result.append(new)

    return result
