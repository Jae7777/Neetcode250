# https://leetcode.com/problems/decode-string/description/

from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                token = deque()
                while stack and stack[-1] != '[':
                    token.appendleft(stack.pop())
                stack.pop()
                repeats = deque()
                while stack and stack[-1].isdigit():
                    repeats.appendleft(stack.pop())
                for _ in range(int("".join(repeats))):
                    stack.append("".join(token))
        return "".join(stack)