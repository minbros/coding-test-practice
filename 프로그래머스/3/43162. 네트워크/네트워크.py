def solution(n, computers):
    from collections import deque
    
    result = 0
    queue = deque()
    indexes = [i for i in range(n)]
    
    while indexes:
        queue.append(indexes[0])
        while queue:
            m = queue.popleft()
            indexes.remove(m)
            for i in indexes:
                if computers[m][i] and i not in queue:
                    queue.append(i)
        result += 1
        
    return result