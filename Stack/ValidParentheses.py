# https://neetcode.io/problems/validate-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            'oc': {
                '(': ')',
                '{': '}',
                '[': ']'
            },
            'co': {
                ')': '(',
                '}': '{',
                ']': '['
            }
        }
        for c in s:
            if c in pairs['oc']:
                stack.append(c)
            elif stack and c == pairs['oc'][stack[-1]]:
                stack.pop()
            elif c in pairs['co']:
                return False
        return not stack