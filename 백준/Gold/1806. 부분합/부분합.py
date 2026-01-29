import sys

input = lambda: sys.stdin.readline()

n, s = map(int, input().split())
seq = list(map(int, input().split()))
prefix = [0]
for i in range(n):
    prefix.append(seq[i] + prefix[-1])

if prefix[-1] < s:
    print(0)
    quit()

# k는 시작과 끝의 인덱스 값 차이
k = 0
for i in range(1, n + 1):
    if prefix[i] >= s:
        k = i - 1
        break

for end in range(k, n):
    for start in range(end - k, end + 1):
        val = prefix[end + 1] - prefix[start]
        if val < s:
            break

        if k > end - start:
            k = end - start

print(k + 1)
