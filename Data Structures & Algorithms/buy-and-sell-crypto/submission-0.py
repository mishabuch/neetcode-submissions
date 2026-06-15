class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Here, we just check if the price of the next day is greater than
        # the previous day, and add all of them up. The sliding window is basically
        # of size 2

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit  
        