import sys

input = lambda: sys.stdin.readline()
lights = {
    '0': 0b1110111,
    '1': 0b0010010,
    '2': 0b1011101,
    '3': 0b1011011,
    '4': 0b0111010,
    '5': 0b1101011,
    '6': 0b1101111,
    '7': 0b1010010,
    '8': 0b1111111,
    '9': 0b1111011
}


def get_counts(a, b):
    return bin(lights[a] ^ lights[b]).count('1')


n, k, p, x = map(int, input().split())
default = str(x).zfill(k)
answer = 0
for num in range(1, n + 1):
    if num == x:
        continue

    target = str(num).zfill(k)
    count = sum(get_counts(d1, d2) for d1, d2 in zip(default, target))
    answer += int(count <= p)

print(answer)
