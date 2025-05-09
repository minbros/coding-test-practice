import sys

input = sys.stdin.readline
jun_money = sung_money = int(input())
jun_stock = sung_stock = 0
check = []

stock_prices = list(map(int, input().split()))
for stock_price in stock_prices:
    if jun_money >= stock_price:
        k = jun_money // stock_price
        jun_money -= stock_price * k
        jun_stock += k

    if len(check) >= 2 and (check[-2] - check[-1]) * (check[-1] - stock_price) <= 0 \
            or len(check) > 0 and check[-1] == stock_price:
        check = [check[-1]]
    check.append(stock_price)

    if len(check) >= 4:
        if check[-2] - check[-1] > 0:
            k = sung_money // stock_price
            sung_money -= stock_price * k
            sung_stock += k
        else:
            sung_money += sung_stock * stock_price
            sung_stock = 0

jun_money += jun_stock * stock_prices[-1]
sung_money += sung_stock * stock_prices[-1]
if jun_money > sung_money:
    print("BNP")
elif jun_money < sung_money:
    print("TIMING")
else:
    print("SAMESAME")
