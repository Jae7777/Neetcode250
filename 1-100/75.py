# https://leetcode.com/problems/sort-colors/description/
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        # [0,0,2,1,1,2]
        for j in range(len(nums)):
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # [0,0,1,1,2,2]
        for j in range(i, len(nums)):
            if nums[j] < 2:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1