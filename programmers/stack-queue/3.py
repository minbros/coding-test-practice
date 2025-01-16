# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False

            stack.pop()

    if len(stack) != 0:
        return False

    return True