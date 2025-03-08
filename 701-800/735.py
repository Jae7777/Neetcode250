# https://leetcode.com/problems/asteroid-collision/

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            broken = False
            while stack and ast <= 0 and stack[-1] > 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    stack.pop()
                    broken = True
                    break
                else:
                    broken = True
                    break
            if not broken:
                stack.append(ast)
            
        return stack