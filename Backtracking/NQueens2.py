# https://leetcode.com/problems/n-queens-ii/
class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()
        def backtrack(r, k):
            if k == n:
                return 1
            res = 0
            for c in range(n):
                if (r + c) not in posDiag and (r - c) not in negDiag and c not in col:
                    posDiag.add((r + c))
                    negDiag.add((r - c))
                    col.add(c)
                    res += backtrack(r + 1, k + 1)
                    posDiag.remove((r + c))
                    negDiag.remove((r - c))
                    col.remove(c)
            return res
        return backtrack(0, 0)