# https://neetcode.io/problems/search-2d-matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, t = 0, len(matrix) - 1
        row = 0
        while b <= t:
            m = (t + b) // 2
            if matrix[m][0] > target:
                t = m - 1
            elif matrix[m][-1] < target:
                b = m + 1
            else:
                row = m
                break
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False