# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    import itertools

    def clear_dungeon(_k, _dungeons):
        for dungeon in _dungeons:
            if _k >= dungeon[0]:
                _k -= dungeon[1]
            else:
                return False

        return True

    for i in range(len(dungeons), 0, -1):
        for perm in list(itertools.permutations(dungeons, i)):
            if clear_dungeon(k, perm):
                return i
            else:
                continue
