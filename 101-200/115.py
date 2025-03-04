# https://leetcode.com/problems/distinct-subsequences/description/
# 2-D DP
# TIME: O(N * M)
# SPACE: O(N * M)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:     
        memo = {}
        def dfs(si, ti):
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            if (si, ti) in memo:
                return memo[(si, ti)]
            a = 0
            if s[si] == t[ti]:
                a = dfs(si + 1, ti + 1)
            b = dfs(si + 1, ti)
            memo[(si, ti)] = a + b
            return memo[(si, ti)]
            
        return dfs(0, 0)