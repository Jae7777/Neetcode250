# https://leetcode.com/problems/unique-paths/description/
# 2-D DP Bottom-Up
# Time: O(M * N)
# Space: O(M * N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                up = paths[i - 1][j] if i - 1 >= 0 else 0
                left = paths[i][j - 1] if j - 1 >= 0 else 0
                paths[i][j] += up + left
        return paths[-1][-1]

# 2-D DP Top-Down
# Time: O(M * N)
# Space: O(M * N)
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