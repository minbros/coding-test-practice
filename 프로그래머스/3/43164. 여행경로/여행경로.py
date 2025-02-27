def solution(tickets):
    from collections import deque
    
    k = len(tickets)
    queue = deque([["ICN", []]])
    
    while queue:
        start, history = queue.popleft()
        depth = len(history)
        if depth == k:
            result = history
            break

        tmp = []
        for i, ticket in enumerate(tickets):
            if i not in history and ticket[0] == start:
                new_history = history.copy()
                new_history.append(i)
                tmp.append([ticket[1], new_history])

        for t in sorted(tmp):
            queue.append(t)
            
    answer = ["ICN"]
    for i in result:
        answer.append(tickets[i][1])
        
    return answer