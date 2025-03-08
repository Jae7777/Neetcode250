# https://neetcode.io/problems/daily-temperatures
# https://leetcode.com/problems/daily-temperatures/description/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                j = stack.pop()[1]
                res[j] = i - j
            stack.append((t, i))
        return res