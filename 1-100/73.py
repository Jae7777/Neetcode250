# https://neetcode.io/problems/set-zeroes-in-matrix
# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List

# O(M * N) time and O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        def fillDirection(i, j, direction):
            while i >= 0 and j >= 0 and i < M and j < N:
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                i += direction[0]
                j += direction[1]
        
        # fill while setting original 0s to inf
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')
                    fillDirection(i - 1, j, (-1, 0))
                    fillDirection(i + 1, j, (1, 0))
                    fillDirection(i, j - 1, (0, -1))
                    fillDirection(i, j + 1, (0, 1))
        
        # revert inf to 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
            