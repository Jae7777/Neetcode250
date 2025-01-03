# https://neetcode.io/problems/find-duplicate-integer
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t, h = nums[0], nums[nums[0]]
        while t != h:
            t = nums[t]
            h = nums[nums[h]]
        t = 0
        while t != h:
            t = nums[t]
            h = nums[h]
        return t