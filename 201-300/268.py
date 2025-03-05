# https://neetcode.io/problems/missing-number
# https://leetcode.com/problems/missing-number/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(1, len(nums) + 1):
            missing ^= i ^ nums[i - 1]
        return missing