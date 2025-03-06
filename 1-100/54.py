# https://neetcode.io/problems/spiral-matrix
# https://leetcode.com/problems/spiral-matrix/description/

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        res = []
        def spiraling(i, j, direction):
            if i < 0 or j < 0 or i >= M or j >= N or matrix[i][j] == -1000:
                return
            res.append(matrix[i][j])
            matrix[i][j] = -1000
            spiraling(i + direction[0], j + direction[1], direction)
            spiraling(i, j + 1, (0, 1))
            spiraling(i + 1, j, (1, 0))
            spiraling(i, j - 1, (0, -1))
            spiraling(i - 1, j, (-1, 0))
        
        spiraling(0, 0, (0, 1))
        return res