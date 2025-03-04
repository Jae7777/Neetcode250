# https://neetcode.io/problems/swim-in-rising-water
# https://leetcode.com/problems/swim-in-rising-water/description/
# graph
# Dijkstra's algorithm
# TIME: O(N * log(N))
# SPACE: O(N)
from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        minElevation = 0
        visited = set()
        while pq:
            elevation, r, c = heapq.heappop(pq)
            minElevation = max(minElevation, elevation)
            visited.add((r, c))
            if r == ROW - 1 and c == COL - 1:
                break
            if r - 1 >= 0 and (r - 1, c) not in visited:
                heapq.heappush(pq, (grid[r - 1][c], r - 1, c))
            if r + 1 < ROW and (r + 1, c) not in visited:
                heapq.heappush(pq, (grid[r + 1][c], r + 1, c))
            if c - 1 >= 0 and (r, c - 1) not in visited:
                heapq.heappush(pq, (grid[r][c - 1], r, c - 1))
            if c + 1 < COL and (r, c + 1) not in visited:
                heapq.heappush(pq, (grid[r][c + 1], r, c + 1))
            
        return minElevation