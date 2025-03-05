# https://neetcode.io/problems/maximum-subarray
# https://leetcode.com/problems/maximum-subarray/description/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for num in nums:
            currSum += num
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum