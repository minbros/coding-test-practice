# 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    a = max([min(x) for x in sizes])
    b = max([max(x) for x in sizes])
    return a * b
