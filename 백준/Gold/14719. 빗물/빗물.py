import sys

input = lambda: sys.stdin.readline()


def count_blocks(height):
    _count = 0
    tmp = 0
    closed = False
    for block in blocks:
        if closed:
            if block >= height:
                _count += tmp
                tmp = 0
            else:
                tmp += 1
        elif not closed and block >= height:
            closed = True

    return _count


h, w = map(int, input().split())
blocks = list(map(int, input().split()))
max_height = max(blocks)

result = 0
for i in range(max(1, min(blocks)), max_height + 1):
    count = count_blocks(i)
    if count < w:
        result += count

print(result)
