import sys

input = lambda: sys.stdin.readline()
lights = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1010010',
    '8': '1111111',
    '9': '1111011'
}


def get_counts(a, b):
    if a == b:
        return 0

    return [d1 != d2 for d1, d2 in zip(lights[a], lights[b])].count(True)


n, k, p, x = map(int, input().split())
default = str(x).zfill(k)
answer = 0
for num in range(1, n + 1):
    target = str(num).zfill(k)
    count = 0
    possible = True
    for default_digit, target_digit in zip(default, target):
        count += get_counts(default_digit, target_digit)
        if count > p:
            possible = False
            break

    answer += int(possible)

print(answer - 1)
