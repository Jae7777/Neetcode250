# https://neetcode.io/problems/two-integer-sum
# https://leetcode.com/problems/two-sum/description/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if target - n in m:
                return [m[target - n], i]
            elif n not in m:
                m[n] = i
        return []