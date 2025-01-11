# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    closet = {}
    for item in clothes:
        _value, _key = item
        if _key in closet:
            closet[_key].append(_value)
        else:
            closet[_key] = [_value]

    arr = []
    for a in closet.values():
        arr.append(len(a) + 1)

    r = 1
    for v in arr:
        r *= v

    return r - 1