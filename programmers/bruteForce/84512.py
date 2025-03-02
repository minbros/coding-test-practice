# 모음 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    dic = ["A", "E", "I", "O", "U"]
    tmp = ["A"]
    word = list(word)
    count = 1

    while word != tmp:
        if len(tmp) != 5:
            tmp.append("A")
            count += 1
        else:
            while True:
                t = tmp.pop()
                if t != "U":
                    tmp.append(dic[dic.index(t) + 1])
                    break

            count += 1

    return count
