# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.sums = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                self.sums[r][c] += self.sums[r-1][c] + self.sums[r][c-1] + matrix[r-1][c-1] - self.sums[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)