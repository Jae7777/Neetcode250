# https://neetcode.io/problems/jump-game
class Solution: # DP, top-down
    def canJump(self, nums: List[int]):
        memo = set()
        def dfs(i):
            maxJump = i + nums[i]
            if maxJump >= len(nums) - 1:
                return True
            if i in memo:
                return False
            while i < maxJump:
                if dfs(maxJump):
                    return True
                maxJump -= 1
            memo.add(i) 
            return False
        return dfs(0)

class Solution: # Greedy
    def canJump(self, nums: List[int]):
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0