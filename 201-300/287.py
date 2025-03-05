# https://neetcode.io/problems/duplicate-integer
# https://leetcode.com/problems/find-the-duplicate-number/description/
# TIME: O(N)
# SPACE: O(1)
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)