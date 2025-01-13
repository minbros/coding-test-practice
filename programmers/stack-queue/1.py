# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    stack = []
    temp = None

    for a in arr:
        if a != temp:
            stack.append(a)
        temp = a

    return stack
