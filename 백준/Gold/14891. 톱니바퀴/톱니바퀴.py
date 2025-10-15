def rotate(wheel: str, direction: int):
    if direction == -1:
        return wheel[1:] + wheel[0]
    elif direction == 1:
        return wheel[7] + wheel[:7]

    return None


wheels = [input() for _ in range(4)]
k = int(input())
for _ in range(k):
    num, dirn = map(int, input().split())
    changes = [''] * 4
    tmp_num, tmp_dirn = num, dirn
    while tmp_num > 1 and wheels[tmp_num - 2][2] != wheels[tmp_num - 1][6]:
        changes[tmp_num - 2] = rotate(wheels[tmp_num - 2], -tmp_dirn)
        tmp_num -= 1
        tmp_dirn *= -1

    tmp_num, tmp_dirn = num, dirn
    while tmp_num < 4 and wheels[tmp_num][6] != wheels[tmp_num - 1][2]:
        changes[tmp_num] = rotate(wheels[tmp_num], -tmp_dirn)
        tmp_num += 1
        tmp_dirn *= -1

    changes[num - 1] = rotate(wheels[num - 1], dirn)
    for i in range(4):
        if changes[i] != '':
            wheels[i] = changes[i]

result = 0
for i in range(3, -1, -1):
    result = (result << 1) | int(wheels[i][0])

print(result)
