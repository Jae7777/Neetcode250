# https://neetcode.io/problems/target-sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, currAmount):
            if i == len(nums):
                if currAmount == target:
                    return 1
                return 0
            if (i, currAmount) in memo:
                return memo[(i, currAmount)]
            a1 = dfs(i + 1, currAmount + nums[i])
            s1 = dfs(i + 1, currAmount - nums[i])
            memo[(i, currAmount)] = a1 + s1
            return memo[(i, currAmount)]
        
        return dfs(0, 0)