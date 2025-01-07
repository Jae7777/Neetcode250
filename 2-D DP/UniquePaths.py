# https://neetcode.io/problems/count-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = {}
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1

            downPaths = 0
            if (r + 1, c) in paths:
                downPaths = paths[(r + 1, c)]
            else:
                downPaths = dfs(r + 1, c)

            rightPaths = 0
            if (r, c + 1) in paths:
                rightPaths = paths[(r, c + 1)]
            else:
                rightPaths = dfs(r, c + 1)
            
            paths[(r, c)] = downPaths + rightPaths
            return paths[(r, c)]

        return dfs(0, 0)