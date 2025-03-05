# https://leetcode.com/problems/combinations/
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        currCombo = []
        def comboBreaker(i):
            if len(currCombo) == k:
                res.append(currCombo[:])
                return
            if i > n:
                return
            currCombo.append(i)
            comboBreaker(i + 1)
            currCombo.pop()
            comboBreaker(i + 1)
        comboBreaker(1)
        return res