# https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        currSum = 0
        l, r = 0, 0
        while r < len(nums):
            currSum += nums[r]
            if currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l] + nums[r]
                l += 1
            else:
                r += 1
        return res if res != float('inf') else 0