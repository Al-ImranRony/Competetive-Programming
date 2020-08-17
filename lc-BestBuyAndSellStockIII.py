# LeetCode Aug challenge 16

def maxProfit(prices) -> int:
    firstBuy, firstProfit, secBuy, maxProfit = float('inf'), 0, float('inf'), 0

    for price in prices:
        firstBuy = min(firstBuy, price)
        firstProfit = max(firstProfit, price - firstBuy)
        secBuy = min(secBuy, price - firstProfit)
        maxProfit = max(maxProfit, price - secBuy)

    return maxProfit

print(maxProfit([3,3,5,0,0,3,1,4]))