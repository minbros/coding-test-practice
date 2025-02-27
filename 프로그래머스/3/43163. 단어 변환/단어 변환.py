def solution(begin, target, words):
    from collections import deque
    
    queue = deque([(begin, 0)])
    k = len(words[0])
    
    while queue:
        word, depth = queue.popleft()
        if word == target:
            return depth
        
        delete = []
        for w in words:
            count = 0
            for i in range(k):
                if word[i] != w[i]:
                    count += 1
            if count == 1:
                delete.append(w)
                queue.append((w, depth + 1))
                
        for d in delete:
            words.remove(d)
    
    return 0