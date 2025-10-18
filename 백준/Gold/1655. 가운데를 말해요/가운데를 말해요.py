import sys
import heapq

input = sys.stdin.readline


class MedianHeap:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add(self, x: int):
        if not self.max_heap or x <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -x)
        else:
            heapq.heappush(self.min_heap, x)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return -self.max_heap[0]


n = int(input())
h = MedianHeap()
for _ in range(n):
    num = int(input())
    h.add(num)
    print(h.get())
