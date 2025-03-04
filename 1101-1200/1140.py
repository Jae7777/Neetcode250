# https://leetcode.com/problems/stone-game-ii/
# 2-D DP
# Time: O(N^2)
# Space: O(N^2)
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        dp = {}
        def dfs(i, m):
            if i == len(piles):
                return 0
            if (i, m) in dp:
                return dp[(i, m)]
            res = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                res = max(res, suffix[i] - dfs(i + x, max(x, m)))
            dp[(i, m)] = res
            return res
        return dfs(0, 1)