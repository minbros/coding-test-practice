# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    dic = [0] * len(nums)

    for num in nums:
        dic[num - 1] += 1

    dic = [d for d in dic if d >= 1]

    if len(nums) // 2 <= len(dic):
        answer = len(dic)
    else:
        answer = len(nums) // 2

    return answer
