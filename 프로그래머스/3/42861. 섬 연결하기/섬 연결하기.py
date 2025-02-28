from collections import defaultdict
import heapq

def solution(n, costs):
    graph = defaultdict(list)
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))
    
    result = 0
    edges = [(cost, 0, end) for end, cost in graph[0]]
    visited = [False] * n
    visited[0] = True
    heapq.heapify(edges)
    while edges:
        cost, start, end = heapq.heappop(edges)
        if not visited[end]:
            visited[end] = True
            result += cost
            
            for next_end, next_cost in graph[end]:
                if not visited[next_end]:
                    heapq.heappush(edges, (next_cost, end, next_end))
                    
    return result
        