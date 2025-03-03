# https://leetcode.com/problems/last-stone-weight-ii/
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        total = sum(stones)
        target = total // 2
        carry = total % 2
        def dfs(i, curr):
            if curr > target:
                return float('inf')
            if curr == target or i == len(stones):
                return target - curr
            if (i, curr) in dp:
                return dp[(i, curr)]
            res = float('inf')
            res = min(dfs(i + 1, curr + stones[i]), dfs(i + 1, curr))
            dp[(i, curr)] = res
            return res
        res = dfs(0, 0)
        return res * 2 + carry
