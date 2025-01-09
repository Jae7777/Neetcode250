# https://neetcode.io/problems/longest-increasing-path-in-matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        memo = {}
        visited = set()
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            visited.add((r, c))
            up = dfs(r - 1, c) if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c] else 0
            down = dfs(r + 1, c) if r + 1 < ROW and matrix[r + 1][c] > matrix[r][c] else 0
            left = dfs(r, c - 1) if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c] else 0
            right = dfs(r, c + 1) if c + 1 < COL and matrix[r][c + 1] > matrix[r][c] else 0
            visited.remove((r, c))
            memo[(r, c)] = 1 + max(up, down, left, right)
            return memo[(r, c)]
        
        maxCount = 0
        for r in range(ROW):
            for c in range(COL):
                maxCount = max(maxCount, dfs(r, c))
        return maxCount