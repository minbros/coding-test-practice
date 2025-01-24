def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    t1 = t2 = t3 = 0
    
    for i in range(len(answers)):
        t1 += int(s1[i % 5] == answers[i])
        t2 += int(s2[i % 8] == answers[i])
        t3 += int(s3[i % 10] == answers[i])
    
    scores = [t1, t2, t3]
    top = max(scores)
    result = [i + 1 for i, x in enumerate(scores) if x == top]
    
    return result