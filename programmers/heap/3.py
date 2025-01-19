# 이중 우선순위 큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    import heapq

    l = len(operations)
    min_heap = []
    max_heap = []
    deleted = [False] * l

    for i in range(l):
        arg, num = operations[i].split()
        num = int(num)

        if arg == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        else:
            if not min_heap or not max_heap:
                continue
            elif num == 1:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[heapq.heappop(max_heap)[1]] = True
            elif num == -1:
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[heapq.heappop(min_heap)[1]] = True

    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)

    print(min_heap, max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    else:
        min_value = heapq.heappop(min_heap)[0]
        max_value = -1 * heapq.heappop(max_heap)[0]
        return [max_value, min_value]