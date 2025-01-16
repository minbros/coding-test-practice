# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    from collections import deque

    q = deque()
    for i, p in enumerate(priorities):
        q.append((p, i))

    c = 0
    while len(q):
        if q[0][0] == max(q)[0]:
            tmp = q.popleft()
            c += 1
            if tmp[1] == location:
                return c
        else:
            q.append(q.popleft())
