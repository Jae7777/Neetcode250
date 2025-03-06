# https://neetcode.io/problems/find-duplicate-integer
# https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t, h = nums[0], nums[nums[0]]
        while t != h:
            t = nums[t]
            h = nums[nums[h]]
        t = 0
        while t != h:
            t = nums[t]
            h = nums[h]
        return t