# https://leetcode.com/problems/jump-game-vii/description/
from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            for j in range(max(farthest + 1, i + minJump), min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    q.append(j)
            farthest = i + maxJump
        return False