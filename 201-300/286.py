# https://neetcode.io/problems/islands-and-treasure
# https://leetcode.com/problems/walls-and-gates/description/
from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        def fillMinDistance(q, r, c, distance):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or grid[r][c] == -1 or grid[r][c] < distance:
                return
            grid[r][c] = distance
            visited.add((r, c))
            q.append((r + 1, c, distance + 1))
            q.append((r - 1, c, distance + 1))
            q.append((r, c + 1, distance + 1))
            q.append((r, c - 1, distance + 1))

        while q:
            newQ = deque()
            while q:
                r, c, d = q.popleft()
                fillMinDistance(newQ, r, c, d)
            q = newQ
