def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][0] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                tmp = max(triangle[i - 1][j - 1], triangle[i - 1][j])
                triangle[i][j] += tmp
                
    return max(triangle[-1])