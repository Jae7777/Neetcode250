# https://leetcode.com/problems/stone-game/
# 2-D DP
# Time: O(N^2)
# Space: O(N^2)
from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r):
            if l == r:
                return piles[l]
            if (l, r) in dp:
                return dp[(l, r)]
            res = 0
            res = max(piles[l] - dfs(l + 1, r), piles[r] - dfs(l, r - 1))
            dp[(l, r)] = res
            return res
        res = dfs(0, len(piles) - 1)
        return True if res > 0 else False

# it's mathematically solved given the constraints
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True