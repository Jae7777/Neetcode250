# https://neetcode.io/problems/find-target-in-rotated-sorted-array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r :
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # left quad
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        

    