# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    l = len(citations)
    citations.sort(reverse=True)
    answer = 0

    for i in range(l):
        # citations[i] 이상이 (i + 1)개 있다.
        tmp = min(citations[i], i + 1)

        if answer >= tmp:
            return answer

        answer = tmp

    return answer
