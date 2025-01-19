# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        combo = []
        def kSum(start, k, currSum):
            if start >= len(nums) or k * nums[start] > target - currSum or k * nums[-1] < target - currSum:
                return
            if k == 2:
                twoSum(currSum, start, len(nums) - 1)
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                combo.append(nums[i])
                kSum(i + 1, k - 1, currSum + nums[i])
                combo.pop()

        def twoSum(currSum, l, r):
            while l < r:
                if currSum + nums[l] + nums[r] < target:
                    l += 1
                elif currSum + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(combo + [nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

        kSum(0, 4, 0)
        return res