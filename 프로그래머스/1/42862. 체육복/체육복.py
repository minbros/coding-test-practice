def solution(n, lost, reserve):
    e_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            e_lost.append(l)
    
    result = n - len(e_lost)
    e_lost.sort()
    reserve.sort()
    
    for l in e_lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            result += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            result += 1
            
    return result