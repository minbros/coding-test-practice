def solution(scoville, K):
    import heapq
    
    count = 0
    heapq.heapify(scoville)
    
    while True:
        tmp = heapq.heappop(scoville)
        if tmp >= K:
            break
        elif len(scoville) == 0:
            count = -1
            break
            
        new = tmp + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, new)
        count += 1
        
    return count