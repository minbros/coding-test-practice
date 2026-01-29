def is_zero(formula):
    num = 0
    symbol = 1
    result = 0
    for char in formula:
        if char == '+':
            result += symbol * num
            symbol = 1
            num = 0
        elif char == '-':
            result += symbol * num
            symbol = -1
            num = 0
        elif char != ' ':
            num = 10 * num + int(char)

    result += num * symbol
    return result == 0


def solve(formula, count):
    global answer
    if count == n:
        if is_zero(formula):
            answer.append(formula)
        return

    # 문자열 추가를 ASCII 순서로 진행
    solve(formula + ' ' + str(count + 1), count + 1)
    solve(formula + '+' + str(count + 1), count + 1)
    solve(formula + '-' + str(count + 1), count + 1)


t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    solve('1', 1)
    print(*answer, sep='\n')
    print()
