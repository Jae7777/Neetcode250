# https://leetcode.com/problems/stone-game-iii/
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]
            res = float('-inf')
            val = 0
            for j in range(i, min(i + 3, len(stoneValue))):
                val += stoneValue[j]
                res = max(res, val - dfs(j + 1))
            dp[i] = res
            return res
        res = dfs(0)
        return "Alice" if res > 0 else "Bob" if res < 0 else "Tie"