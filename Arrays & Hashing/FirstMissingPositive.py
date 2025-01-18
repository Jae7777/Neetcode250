# https://leetcode.com/problems/first-missing-positive/description/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num <= len(nums) and num > 0:
                if num == nums[num - 1]:
                    i += 1
                    continue
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                nums[i] = float('inf')
                i += 1
        smallest = 1
        for num in nums:
            if num == smallest:
                smallest += 1
        return smallest