class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [0 for _ in range(len(prices))]
        # minPrice = prices[0]
        # for i in range(1, len(prices)):
        #     dp[i] = max(dp[i - 1], prices[i] - minPrice)
        #     minPrice = min(minPrice, prices[i])
        # return dp[-1]

        maxProfit = 0
        minCost = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minCost)
            minCost = min(minCost, prices[i])
        return maxProfit
