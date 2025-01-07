# https://neetcode.io/problems/partition-equal-subset-sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2
        sums = set([0, nums[0]])
        for i in range(1, len(nums)):
            for s in list(sums):
                if s + nums[i] < target:
                    sums.add(s + nums[i])
                elif s + nums[i] > target:
                    continue
                else:
                    return True
        return False
