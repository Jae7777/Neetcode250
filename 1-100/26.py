# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        l, r = 1, 1
        while r < len(nums):
            if nums[r] > prev:
                nums[l] = nums[r]
                prev = nums[l]
                l += 1
                r += 1
            else:
                r += 1
        return l