def solution(m, n, puddles):
    table = [[0 for _ in range(m)] for _ in range(n)]
    table[0][0] = 1
    for x, y in puddles:
        table[y - 1][x - 1] = -1
        
    for i in range(n):
        for j in range(m):
            if table[i][j] == -1:
                continue
                
            if i > 0 and table[i - 1][j] != -1:
                table[i][j] += table[i - 1][j]
            if j > 0 and table[i][j - 1] != -1:
                table[i][j] += table[i][j - 1]
                    
    return table[-1][-1] % 1000000007