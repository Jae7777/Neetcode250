# https://leetcode.com/problems/longest-increasing-subsequence/submissions/1562051194/
# 1-D DP
# Time: O(n^2)
# Space: O(n)
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    sequence[i] = max(sequence[i], sequence[j] + 1)
        return max(sequence)
