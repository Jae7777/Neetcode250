# https://leetcode.com/problems/perfect-squares/description/
# bottom up 1-D DP
# Time: O(N^2)
# Space: O(N)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                sq = j ** 2
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]
    
# top down 1-D DP
# Time: O(N^2)
# Space: O(N)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def dfs(k):
            if k == 0:
                return 0
            if k == 1:
                return 1
            if k in dp:
                return dp[k]
            res = float('inf')
            for i in range(1, k):
                if i ** 2 > k:
                    break
                res = min(res, dfs(k - i ** 2) + 1)
            dp[k] = res
            return res
        res = dfs(n)
        return res