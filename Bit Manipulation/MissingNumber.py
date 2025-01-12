# https://neetcode.io/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # take xor and the complement?
        missing = 0
        for i in range(1, len(nums) + 1):
            missing ^= i ^ nums[i - 1]
        return missing