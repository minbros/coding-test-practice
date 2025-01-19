def solution(jobs):
    import heapq
    from collections import deque
    
    i = 0
    time = 0
    wait = []
    times = []
    l = len(jobs)

    heapq.heapify(jobs) 
    
    while len(times) < l:
        while len(jobs) and jobs[0][0] <= time:
            new = heapq.heappop(jobs)
            heapq.heappush(wait, (new[1], new[0], i))
            i += 1
                
        if len(wait):
            t = heapq.heappop(wait)
            time += t[0]
            times.append(time - t[1])
        else:
            time += 1
    
    return sum(times) // l