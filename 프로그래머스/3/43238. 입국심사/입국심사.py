def solution(n, times):
    k = min(times)
    left = k
    right = k * n
    result = 0
    while left + 1 != right:
        middle = (left + right) // 2
        tmp = [middle // t for t in times]
        if sum(tmp) >= n:
            result = middle
            right = middle
        else:
            left = middle
            
    return result