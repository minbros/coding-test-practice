def solution(brown, yellow):
    k = (brown + 4) // 2
    for x in range(3, k - 2):
        y = k - x
        if (x - 2) * (y - 2) == yellow:
            return sorted([x, y], reverse=True)