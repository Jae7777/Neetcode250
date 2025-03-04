# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# 2-D DP
# TIME: O(N)
# SPACE: O(N)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0
            if (i, isBuy) in memo:
                return memo[(i, isBuy)]

            cdProfit = dfs(i + 1, isBuy)
            profit = 0
            if isBuy:
                profit = dfs(i + 1, not isBuy) - prices[i]
            else:
                profit = dfs(i + 2, not isBuy) + prices[i]
            memo[(i, isBuy)] = max(profit, cdProfit)

            return memo[(i, isBuy)]

        return dfs(0, True)