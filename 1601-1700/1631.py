# https://leetcode.com/problems/path-with-minimum-effort/
# TIME: O(n * log(n)), n is the number of cells in heights
# SPACE: O(n)
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW, COL = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        visited = set()
        res = 0
        while pq:
            effort, r, c = heapq.heappop(pq)
            res = max(res, effort)
            if r == ROW - 1 and c == COL - 1:
                break
            visited.add((r, c))
            currHeight = heights[r][c]
            cells = [
                (abs(heights[r-1][c] - currHeight), r - 1, c) if r - 1 >= 0 else None,
                (abs(heights[r+1][c] - currHeight), r + 1, c) if r + 1 < ROW else None,
                (abs(heights[r][c-1] - currHeight), r, c - 1) if c - 1 >= 0 else None,
                (abs(heights[r][c+1] - currHeight), r, c + 1) if c + 1 < COL else None,
            ]
            for cell in cells:
                if cell and (cell[1], cell[2]) not in visited:
                    heapq.heappush(pq, cell)
        return res