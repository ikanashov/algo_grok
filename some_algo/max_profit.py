# N
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit


# N x N
def max_profit_2(prices: list[int]) -> int:
    left = 0
    max_diff = 0

    while left < len(prices):
        right = left
        while right < len(prices):
            if prices[right] - prices[left] > max_diff:
                max_diff = prices[right] - prices[left]
            right += 1
        left += 1

    return max_diff
