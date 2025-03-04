# https://leetcode.com/problems/house-robber/submissions/1562047790/
# 1-D DP
# TIME: O(N)
# SPACE: O(1)
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        nums[2] = max(nums[0] + nums[2], nums[2])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i] + nums[i - 3])
        return max(nums[-1], nums[-2])