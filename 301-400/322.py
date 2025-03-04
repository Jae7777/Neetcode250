# https://leetcode.com/problems/coin-change/
# 1-D DP
# TIME: O(N * amount)
# SPACE: O(amount)
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsNeeded = [float('inf')] * (amount + 1)
        coinsNeeded[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    coinsNeeded[a] = min(coinsNeeded[a], coinsNeeded[a - coin] + 1)
        return coinsNeeded[amount] if coinsNeeded[amount] != float('inf') else -1