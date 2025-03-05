# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        def bt(i, k, currSum):
            if k == 0:
                return True
            if currSum == target:
                return bt(0, k - 1, 0)
            for j in range(i, len(nums)):
                if j > 0 and not used[j - 1] and nums[j] == nums[j - 1]:
                    continue
                if not used[j] and currSum + nums[j] <= target:
                    used[j] = True
                    if bt(j + 1, k, currSum + nums[j]):
                        return True
                    used[j] = False
            return False
        return bt(0, k, 0)