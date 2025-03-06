# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set([nums[0]])
        l, r = 0, 1
        while r < k and r < len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            r += 1
        while r < len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            s.remove(nums[l])
            l += 1
            r += 1
        return False