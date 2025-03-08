# https://leetcode.com/problems/rotate-array/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def flip(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k %= len(nums)
        flip(0, len(nums) - k - 1)
        flip(len(nums) - k, len(nums) - 1)
        flip(0, len(nums) - 1)