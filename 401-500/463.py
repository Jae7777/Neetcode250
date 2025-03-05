# https://leetcode.com/problems/island-perimeter/
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            if r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return 1
            visited.add((r, c))
            return dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res += dfs(r, c)
        return res