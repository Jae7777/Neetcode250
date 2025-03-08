# https://leetcode.com/problems/construct-quad-tree/
"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def QUADBIKE(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                return Node(grid[x1][y1] == 1, True, None, None, None, None)
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            topLeft = QUADBIKE(x1, y1, mid_x, mid_y)
            topRight = QUADBIKE(x1, mid_y + 1, mid_x, y2)
            bottomLeft = QUADBIKE(mid_x + 1, y1, x2, mid_y)
            bottomRight = QUADBIKE(mid_x + 1, mid_y + 1, x2, y2)
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                return Node(topLeft.val, True, None, None, None, None)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        return QUADBIKE(0, 0, len(grid) - 1, len(grid) - 1)