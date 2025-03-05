# https://neetcode.io/problems/subsets
# https://leetcode.com/problems/subsets/description/
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [subset + [n] for subset in res]
        return res