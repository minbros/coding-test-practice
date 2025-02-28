def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def solution(n, costs):
    result = []
    edges = sorted([(cost, start, to) for start, to, cost in costs])
    parent = [x for x in range(n)]
    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            parent[find(parent, v)] = u
            result.append(cost)
        
        if len(result) == n - 1:
            return sum(result)