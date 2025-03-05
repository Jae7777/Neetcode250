# https://neetcode.io/problems/single-number
# https://leetcode.com/problems/single-number/description/
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res