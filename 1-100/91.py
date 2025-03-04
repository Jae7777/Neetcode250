# https://leetcode.com/problems/decode-ways/
# 1-D DP
# Time: O(N)
# Space: O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        digit1 = set(['1', '2'])
        digit2 = set(['0', '1', '2', '3', '4', '5', '6'])
        cache = {len(s): 1} # initially one way to decode
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cache[i] = 0
            else:
                cache[i] = cache[i + 1]
            if i + 1 < len(s) and (s[i] == '1' or (s[i] in digit1 and s[i + 1] in digit2)):
                cache[i] += cache[i + 2]
        return cache[0]