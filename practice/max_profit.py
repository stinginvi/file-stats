def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
# 记录最低价出现的位置写法
# def max_profit_with_days(prices):
#     min_price = float("inf")
#     min_day = 0
#     best = 0
#     buy_day = sell_day = 0
#
#     for i, price in enumerate(prices):
#         if price < min_price:          # 新的最低买入点
#             min_price = price
#             min_day = i
#         if price - min_price > best:   # 今天卖更赚
#             best = price - min_price
#             buy_day, sell_day = min_day, i
#
#     return best, buy_day, sell_day
# 关键是：最低价出现的位置也要记下来，否则知道赚多少，却不知道哪天买的。

if __name__ == "__main__":
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([], 0),
    ]
    for prices, expected in cases:
        result = max_profit(prices)
        ok = "✅" if result == expected else "❌"
        print(f"{ok} {prices} → {result}  期望 {expected}")