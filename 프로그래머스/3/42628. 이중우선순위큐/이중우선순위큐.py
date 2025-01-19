def solution(operations):
    import heapq
    
    l = len(operations)
    minQ = []
    maxQ = []
    deleted = [False] * l
    
    for i in range(l):
        arg, num = operations[i].split()
        num = int(num)
        
        if arg == 'I':
            heapq.heappush(minQ, (num, i))
            heapq.heappush(maxQ, (-num, i))
        else:
            if not minQ or not maxQ:
                continue
            elif num == 1:
                while maxQ and deleted[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    deleted[heapq.heappop(maxQ)[1]] = True
            elif num == -1:
                while minQ and deleted[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    deleted[heapq.heappop(minQ)[1]] = True

    while maxQ and deleted[maxQ[0][1]]:
        heapq.heappop(maxQ)
    while minQ and deleted[minQ[0][1]]:
        heapq.heappop(minQ)
    
    if not minQ or not maxQ:
        return [0, 0]
    else:
        min = heapq.heappop(minQ)[0]
        max = -1 * heapq.heappop(maxQ)[0]
        return [max, min]