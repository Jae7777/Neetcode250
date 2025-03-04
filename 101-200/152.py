# https://leetcode.com/problems/maximum-product-subarray/submissions/1562059298/
# 1-D DP
# Time: O(N)
# Space: O(1)
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algo
        res = currMin = currMax = nums[0]
        for num in nums[1:]:
            tmp = currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp * num, currMin * num, num)
            res = max(res, currMax)
        return res