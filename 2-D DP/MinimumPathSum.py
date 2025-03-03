# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        INF = float('inf')
        for i in range(ROW):
            for j in range(COL):
                up = grid[i - 1][j] if i - 1 >= 0 else INF
                left = grid[i][j - 1] if j - 1 >= 0 else INF
                grid[i][j] += min(up, left) if up != INF or left != INF else 0
        return grid[ROW - 1][COL - 1]