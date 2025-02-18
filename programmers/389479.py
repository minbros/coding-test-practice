# 서버 증설 횟수
# https://school.programmers.co.kr/learn/courses/30/lessons/389479

def solution(players, m, k):
    ext = []
    count = 0
    for t in range(len(players)):
        while ext and ext[0] == t:
            ext.pop(0)

        exceed = (players[t] - m * len(ext))
        for _ in range(exceed // m):
            ext.append(t + k)
            count += 1

    return count
