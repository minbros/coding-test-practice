from itertools import product

def solution(N, number):
    dp = [set()]
    for k in range(1, 9):
        tmp = set()
        tmp.add(int(str(N) * k))
        
        a = k - 1
        b = 1
        ways = []
        while a >= b:
            ways.append((a, b))
            a -= 1
            b += 1
        
        for i1, i2 in ways:
            for x, y in product(dp[i1], dp[i2]):
                tmp.add(x + y)
                if x != y:
                    tmp.add(abs(x - y))
                tmp.add(x * y)
                if x // y != 0:
                    tmp.add(x // y)
                if y // x != 0:
                    tmp.add(y // x)
        
        check = set()
        for i in range(1, k):
            check |= dp[i]

        tmp -= check
        if number in tmp:
            print(dp)
            return k
        
        dp.append(tmp)
    
    return -1