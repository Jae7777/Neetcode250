# https://neetcode.io/problems/duplicate-integer
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)