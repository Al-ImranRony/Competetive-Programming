# LeetCode Sept challenge 18

def maxProfit(prices) -> int:
    buy, maxProfit = float('inf'), 0
    for price in prices:
        buy = min(buy, price)
        maxProfit = max(maxProfit, price-buy)
        
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([3,3,5,0,0,3,1,4]))