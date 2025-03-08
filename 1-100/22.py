# https://neetcode.io/problems/generate-parentheses
# https://leetcode.com/problems/generate-parentheses/description/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def populate(o, c):
            if o == c == n:
                res.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                populate(o + 1, c)
                stack.pop()
            if c < o:
                stack.append(')')
                populate(o, c + 1)
                stack.pop()
        populate(0, 0)
        return res
