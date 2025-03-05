# https://leetcode.com/problems/permutations-ii/
from typing import List
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    perm.append(num)
                    dfs()
                    count[num] += 1
                    perm.pop()
        dfs()
        return res