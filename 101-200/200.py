# https://neetcode.io/problems/count-number-of-islands
# https://leetcode.com/problems/number-of-islands/description/
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0
        def exploreIsland(r, c):
            if grid[r][c] == '0':
                return
            visited.add((r, c))
            if r - 1 >= 0 and (r - 1, c) not in visited:
                exploreIsland(r - 1, c)
            if r + 1 < ROW and (r + 1, c) not in visited:
                exploreIsland(r + 1, c)
            if c - 1 >= 0 and (r, c - 1) not in visited:
                exploreIsland(r, c - 1)
            if c + 1 < COL and (r, c + 1) not in visited:
                exploreIsland(r, c + 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1' and (r, c) not in visited:
                    exploreIsland(r, c)
                    res += 1
        return res