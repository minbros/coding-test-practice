from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    starts = [1]
    visited = [False] * (n + 1)
    visited[0] = True
    visited[1] = True
    while not all(visited):
        result = 0
        tmp = []
        for s in starts:
            for v in graph[s]:
                if not visited[v]:
                    visited[v] = True
                    tmp.append(v)
                    result += 1
        
        starts = tmp
    
    return result
                    