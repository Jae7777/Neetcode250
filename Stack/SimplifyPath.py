# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ignore = set(['', '.'])
        for token in path.split('/'):
            if token in ignore:
                continue
            if token == '..':
                if stack:
                    stack.pop()
                    stack.pop()
            else:
                stack.append('/')
                stack.append(token)
        if not stack:
            return "/"
        return "".join(stack)
        