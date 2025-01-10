# https://neetcode.io/problems/jump-game-ii
class Solution: # DP, top-down
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            target = i + nums[i]
            minJump = float('inf')
            while i < target:
                minJump = min(minJump, dfs(target))
                target -= 1
            memo[i] = minJump + 1
            return memo[i]
        return dfs(0)
    
class Solution: # Greedy
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            jumps += 1
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump 
        return jumps