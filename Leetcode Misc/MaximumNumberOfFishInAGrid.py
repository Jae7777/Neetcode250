# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/submissions/1522726086/
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def searchIsland(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0
            fish += searchIsland(r - 1, c)
            fish += searchIsland(r + 1, c)
            fish += searchIsland(r, c - 1)
            fish += searchIsland(r, c + 1)
            return fish
        maxFish = 0
        for r in range(ROW):
            for c in range(COL):
                maxFish = max(maxFish, searchIsland(r, c))
        return maxFish