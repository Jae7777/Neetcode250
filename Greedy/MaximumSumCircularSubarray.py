# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, currMax = float('-inf'), 0
        globMin, currMin = float('inf'), 0
        total = sum(nums)
        for num in nums:
            currMax += num
            globMax = max(globMax, currMax)
            if currMax < 0:
                currMax = 0
            currMin += num
            globMin = min(globMin, currMin)
            if currMin > 0:
                currMin = 0
        if total - globMin == 0:
            return globMax
        return max(globMax, total - globMin)
            