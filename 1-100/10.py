# https://leetcode.com/problems/regular-expression-matching/description/
# 2-D DP
# TIME: O(N^2)
# SPACE: O(N^2)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        memo = {}
        def dfs(i, j):
            if j >= P:
                return i == S
            if (i, j) in memo:
                return memo[(i, j)]
            match = i < S and (s[i] == p[j] or p[j] == '.')
            if j + 1 < P and p[j + 1] == '*':
                match = dfs(i, j + 2) or (match and dfs(i + 1, j))
                memo[(i, j)] = match
                return match
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)
