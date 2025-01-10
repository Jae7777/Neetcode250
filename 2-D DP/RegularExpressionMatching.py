# https://neetcode.io/problems/regular-expression-matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if i >= len(s) or j >= len(p):
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            matches = False
            if j + 1 < len(p) and p[j + 1] == '*':
                while i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    matches ^= dfs(i, j + 2)
                    i += 1
                matches ^= dfs(i, j + 2)
            elif p[j] == '.' or s[i] == p[j]:
                matches ^= dfs(i + 1, j + 1)
            memo[(i, j)] = matches
            return memo[(i, j)]

        return dfs(0, 0)
