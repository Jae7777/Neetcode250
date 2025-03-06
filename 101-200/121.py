# https://neetcode.io/problems/buy-and-sell-crypto
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = float('inf')
        for price in prices:
            res = max(res, price - lowest)
            lowest = min(lowest, price)
        return res