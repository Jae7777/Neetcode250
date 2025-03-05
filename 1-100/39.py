# https://neetcode.io/problems/combination-target-sum
# https://leetcode.com/problems/combination-sum/description/
from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def buildSum(start, currSum, combo):
            print(start, combo)
            if currSum == target:
                res.append(combo)
                return
            if currSum > target:
                return
            for i, n in enumerate(nums[start:]):
                if currSum + n <= target:
                    buildSum(i + start, currSum + n, combo + [n])
                else:
                    continue

        buildSum(0, 0, [])
        return res