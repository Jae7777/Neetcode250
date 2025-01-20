# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r -= 1
            elif nums[m] < target:
                l += 1
            else:
                return m
        return m + 1 if nums[m] < target else m