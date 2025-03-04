# https://leetcode.com/problems/coin-change-ii/
# 2-D DP
# TIME: O(N * amount)
# SPACE: O(amount)
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount + 1)
        memo[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                memo[j] += memo[j - coins[i]] if j - coins[i] >= 0 else 0
        return memo[amount]