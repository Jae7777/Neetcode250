# https://neetcode.io/problems/n-queens
# https://leetcode.com/problems/n-queens/
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag, negDiag, col = set(), set(), set()
        queens = set()
        def dfs(r):
            if r == n:
                res.append([])
                for r in range(n):
                    row = []
                    for c in range(n):
                        row.append('Q' if (r, c) in queens else '.')
                    res[-1].append("".join(row))
                
            for c in range(n):
                if r + c not in posDiag and r - c not in negDiag and c not in col:
                    queens.add((r, c))
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    col.add(c)
                    dfs(r + 1)
                    queens.remove((r, c))
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    col.remove(c)
        dfs(0)
        return res
