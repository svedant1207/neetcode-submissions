class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        maxp = 0

        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxp = max(profit, maxp)

        return maxp

