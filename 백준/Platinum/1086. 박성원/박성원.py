import sys

input = lambda: sys.stdin.readline()


def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    k = int(input())

    dp = [[0] * k for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][nums[i] % k] = 1

    for visited in range(1, 1 << n):
        cur_digits = get_digits(n, visited, nums)
        mod = (10 ** cur_digits) % k
        for i in range(n):
            if visited & (1 << i):
                continue

            new_visited = visited | (1 << i)
            new_mod = (mod * (nums[i] % k)) % k
            for j in range(k):
                if dp[visited][j] == 0:
                    continue

                dp[new_visited][(j + new_mod) % k] += dp[visited][j]

    p = dp[-1][0]
    q = sum(dp[-1])
    gcd = euclidean(p, q)
    print(f"{p // gcd}/{q // gcd}")


def get_digits(n, visited, nums):
    result = 0
    for i in range(n):
        if not (visited & (1 << i)):
            continue

        result += len(str(nums[i]))

    return result


def euclidean(a, b):
    r = a % b
    if r == 0:
        return b
    return euclidean(b, r)


if __name__ == "__main__":
    main()
