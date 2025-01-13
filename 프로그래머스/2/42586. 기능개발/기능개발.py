def solution(progresses, speeds):
    import math
    from collections import deque

    days = deque()
    for p, s in zip(progresses, speeds):
        d = math.ceil((100 - p) / s)
        days.append(d)

    result = []
    while len(days) != 0:
        c = 1
        tmp = days.popleft()
        
        while len(days) != 0 and days[0] <= tmp:
            days.popleft()
            c += 1
        
        result.append(c)
    
    return result