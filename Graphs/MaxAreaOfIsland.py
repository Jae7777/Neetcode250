# https://neetcode.io/problems/max-area-of-island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        def getArea(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            return 1 + getArea(r-1, c) + getArea(r+1, c) + getArea(r, c-1) + getArea(r, c+1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, getArea(r, c))
        return maxArea