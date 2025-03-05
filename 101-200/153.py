# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l] and nums[m] <= nums[r]:
                res = min(res, nums[l])
                r = m - 1
            elif nums[m] >= nums[r] and nums[m] <= nums[l]:
                res = min(res, nums[r])
                l = m + 1
            elif nums[m] > nums[l] and nums[m] > nums[r]:
                res = min(res, nums[r])
                l = m + 1
            elif nums[m] < nums[l] and nums[m] < nums[r]:
                res = min(res, nums[m])
                r = m - 1
        return res