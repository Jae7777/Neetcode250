# https://leetcode.com/problems/combination-sum-iv/
# 1-D DP
# Time: O(N * target)
# Space: O(target)
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(currSum):
            if currSum in dp:
                return dp[currSum]
            if currSum == target:
                return 1
            count = 0
            for num in nums:
                if currSum + num <= target:
                    count += dfs(currSum + num)
            dp[currSum] = count
            return count
        return dfs(0)