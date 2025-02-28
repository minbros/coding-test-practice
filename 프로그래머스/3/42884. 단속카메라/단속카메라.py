def solution(routes):
    idx = 0
    result = 0
    routes.sort()
    print(routes)
    while idx < len(routes):
        cur = routes[idx]
        for i in range(idx + 1, len(routes)):
            a = max(cur[0], routes[i][0])
            b = min(cur[1], routes[i][1])
            print((a, b))
            if a > b:
                break
            else:
                cur = [a, b]
                idx += 1
        
        idx += 1
        result += 1
        print(idx)
    
    return result