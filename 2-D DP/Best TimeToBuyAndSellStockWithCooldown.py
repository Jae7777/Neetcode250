# https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in memo:
                return memo[(i, isBuy)]

            cdProfit = dfs(i + 1, isBuy)
            if isBuy:
                profit = dfs(i + 1, not isBuy) - prices[i]
                memo[(i, isBuy)] = max(profit, cdProfit)
            else:
                profit = dfs(i + 2, not isBuy) + prices[i]
                memo[(i, isBuy)] = max(profit, cdProfit)

            return memo[(i, isBuy)]

        return dfs(0, True)