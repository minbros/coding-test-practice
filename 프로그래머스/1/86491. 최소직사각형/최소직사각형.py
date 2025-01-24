def solution(sizes):
    a = max([min(x) for x in sizes])
    b = max([max(x) for x in sizes])
    return a * b