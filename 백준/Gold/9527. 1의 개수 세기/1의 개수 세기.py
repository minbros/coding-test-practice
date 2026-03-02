import sys

input = lambda: sys.stdin.readline()

# 0부터 x까지 이진수의 1의 총 개수
def get_count(x):
    count = 0
    div = 2
    while 2 * x >= div:
        val1 = ((x + 1) // div) * (div // 2)
        val2 = (x + 1) % div - div // 2
        count += val1 + max(val2, 0)
        div *= 2
        
    return count

a, b = map(int, input().split())
print(get_count(b) - get_count(a - 1))
