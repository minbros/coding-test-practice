from collections import defaultdict
from collections import deque

def drop(graph):
    return drop_item(graph, 1, [])

def drop_item(graph, node, visited):
    if len(graph[node]) == 0:
        return (visited, node)
    
    visited.append(node)
    return drop_item(graph, graph[node][0], visited)

def optimal(c, t):
    result = [1] * c
    cur = c
    idx = 0
    while cur < t:
        if result[idx] < 3:
            result[idx] += 1
            cur += 1
        else:
            idx += 1
    
    return result
    
def solution(edges, target):
    graph = defaultdict(deque)
    for a, b in edges:
        graph[a].append(b)
    
    for key, value in graph.items():
        graph[key] = deque(sorted(value))
    
    count = [0] * (len(edges) + 1)
    nodes = []
    while True:
        visited, node = drop(graph)
        for x in visited:
            graph[x].append(graph[x].popleft())
        
        if target[node - 1] == count[node - 1]:
            return [-1]
        
        count[node - 1] += 1
        nodes.append(node)
        finished = True
        
        for i in range(len(count)):
            if count[i] < target[i] // 3 + int(target[i] % 3 != 0):
                finished = False
                break
                
        if finished:
            break
    
    optimals = {}
    for i in range(len(target)):
        if target[i] == 0:
            continue
        
        optimals[i + 1] = optimal(count[i], target[i])
        
    answer = []
    for node in nodes:
        answer.append(optimals[node].pop())
    
    return answer