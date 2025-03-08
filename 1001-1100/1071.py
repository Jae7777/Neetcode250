# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# variation of euclid's algorithm
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        i = 0
        while i < len(str1):
            if i + len(str2) <= len(str1) and str1[i:i+len(str2)] == str2:
                i += len(str2)
            else:
                break
        if i == 0:
            return ""
        if i == len(str1):
            return str2
        return self.gcdOfStrings(str1[i:], str2)
        
