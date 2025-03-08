# https://neetcode.io/problems/evaluate-reverse-polish-notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y, 
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(operators[t](x, y))
        return stack[-1]