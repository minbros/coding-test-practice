from collections import deque
from collections import defaultdict

def solution(land):
    m = len(land[0])
    n = len(land)
    oils = defaultdict(int)
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if not visited[j][i] and land[j][i] == 1:
                oil = 0
                cols = set()
                queue = deque([(j, i)])
                visited[j][i] = True
                while queue:
                    r, c = queue.popleft()
                    if c > 0 and land[r][c - 1] and not visited[r][c - 1]:
                        queue.append((r, c - 1))
                        visited[r][c - 1] = True
                    if c < m - 1 and land[r][c + 1] and not visited[r][c + 1]:
                        queue.append((r, c + 1))
                        visited[r][c + 1] = True
                    if r > 0 and land [r - 1][c] and not visited[r - 1][c]:
                        queue.append((r - 1, c))
                        visited[r - 1][c] = True
                    if r < n - 1 and land[r + 1][c] and not visited[r + 1][c]:
                        queue.append((r + 1, c))
                        visited[r + 1][c] = True
                    
                    oil += 1
                    cols.add(c)
                    
                for col in cols:
                    oils[col] += oil

    return max(oils.values())
                