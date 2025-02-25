def solution(maps):
    from collections import deque
    
    que = deque()
    que.append((0, 0, 1))
    visited = [[False for col in range(len(maps[0]))] for row in range(len(maps))]
    
    while que:
        y, x, depth = que.popleft()
        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            return depth
        
        if not visited[y][x]:
            visited[y][x] = True
            if y > 0 and maps[y - 1][x] == 1:
                que.append((y - 1, x, depth + 1))
            if y < len(maps) - 1 and maps[y + 1][x] == 1:
                que.append((y + 1, x, depth + 1))
            if x > 0 and maps[y][x - 1] == 1:
                que.append((y, x - 1, depth + 1))
            if x < len(maps[0]) - 1 and maps[y][x + 1] == 1:
                que.append((y, x + 1, depth + 1))
        
    return -1
    