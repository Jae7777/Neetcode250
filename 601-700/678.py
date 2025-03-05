# https://neetcode.io/problems/valid-parenthesis-string
# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0, 0
        for c in s:
            if c == '(':
                openMin += 1
                openMax += 1
            if c == ')':
                openMin -= 1
                openMax -= 1
            if c == '*':
                openMin -= 1
                openMax += 1
            if openMax < 0:
                return False
            openMin = max(openMin, 0)
        return openMin == 0