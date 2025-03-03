# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if grid[ROW - 1][COL - 1] == 1 or grid[0][0] == 1:
            return 0
        grid[0][0] = -1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    continue
                up = grid[i - 1][j] if i - 1 >= 0 and grid[i - 1][j] != 1 else 0
                left = grid[i][j - 1] if j - 1 >= 0 and grid[i][j - 1] != 1 else 0
                grid[i][j] += up + left
        return -grid[ROW - 1][COL - 1]