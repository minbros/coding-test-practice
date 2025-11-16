import sys

input = lambda: sys.stdin.readline()


def valid():
    x_count = game.count('X')
    o_count = game.count('O')
    if x_count - o_count not in (0, 1):
        return False

    x_line_count = o_line_count = 0
    for i in range(3):
        j = 3 * i
        x_line_count += (int(game[i] == game[i + 3] == game[i + 6] == 'X') +
                         int(game[j] == game[j + 1] == game[j + 2] == 'X'))
        o_line_count += (int(game[i] == game[i + 3] == game[i + 6] == 'O') +
                         int(game[j] == game[j + 1] == game[j + 2] == 'O'))

    x_line_count += int(game[0] == game[4] == game[8] == 'X') + int(game[2] == game[4] == game[6] == 'X')
    o_line_count += int(game[0] == game[4] == game[8] == 'O') + int(game[2] == game[4] == game[6] == 'O')
    if (x_line_count != 0 and x_count == o_count) or (o_line_count != 0 and x_count > o_count):
        return False

    if x_line_count + o_line_count == 0 and x_count + o_count < 9:
        return False

    return True


while True:
    game = input().strip()
    if game == 'end':
        break

    print('valid' if valid() else 'invalid')
