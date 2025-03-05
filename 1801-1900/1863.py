# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        currSubset = []
        def backtrack(i):
            if i == len(nums):
                nonlocal res
                xorSum = 0
                for num in currSubset:
                    xorSum ^= num
                res += xorSum
                return
            currSubset.append(nums[i])
            backtrack(i + 1)
            currSubset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res