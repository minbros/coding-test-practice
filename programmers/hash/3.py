import ast
import collections


def solution(phone_book: list):
    phone_book.sort()

    for i in range(len(phone_book)):
        for number in phone_book[i + 1:]:
            if number[0] != phone_book[i][0]:
                break

            print(phone_book[i], number)

            if number.startswith(phone_book[i]):
                return False

    return True


p = ast.literal_eval(input())
print(solution(p))
