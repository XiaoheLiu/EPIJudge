from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    profit = 0
    temp_min = float('inf')

    for price in prices:
        current_profit = price - temp_min
        profit = max(profit, current_profit)
        temp_min = min(price, temp_min)

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
