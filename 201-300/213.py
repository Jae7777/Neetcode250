# https://leetcode.com/problems/house-robber-ii/description/
# 1-D DP
# TIME: O(N)
# SPACE: O(N)
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        nums1 = nums[:len(nums)-1]
        nums1[2] += nums1[0]
        for i in range(3, len(nums1)):
            nums1[i] = max(nums1[i] + nums1[i - 2], nums1[i] + nums1[i - 3])
        
        nums2 = nums[1:]
        nums2[2] += nums2[0]
        for i in range(3, len(nums2)):
            nums2[i] = max(nums2[i] + nums2[i - 2], nums2[i] + nums2[i - 3])

        return max(nums1[-1], nums2[-1], nums1[-2], nums2[-2])