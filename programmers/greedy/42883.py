# 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    cur = 0
    maximum = max(number)
    count = k
    limit = len(number) - k
    result = ""

    while count > 0 and len(result) < limit:
        if number[cur] == maximum:
            result += number[cur]
            cur += 1
            continue

        is_checked = True
        for idx in range(1, count + 1):
            if number[cur] < number[cur + idx]:
                cur += idx
                count -= idx
                is_checked = False
                break

        if is_checked:
            result += number[cur]
            cur += 1

    if len(result) < limit:
        result += number[-(limit - len(result)):]

    return result
