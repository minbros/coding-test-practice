# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    result = 0
    left = 0
    right = len(people) - 1
    people.sort()

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        result += 1

    return result
