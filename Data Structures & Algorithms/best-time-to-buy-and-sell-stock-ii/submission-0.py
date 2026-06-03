class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] > current_price:
                profit += prices[i] - current_price
            current_price = prices[i]
        return profit

        