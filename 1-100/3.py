# https://neetcode.io/problems/longest-substring-without-duplicates
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        sset = set()
        res = 0
        while r < len(s):
            lc, rc = s[l], s[r] 
            if rc not in sset:
                res = max(res, r - l + 1)
                r += 1
                sset.add(rc)
            else:
                sset.remove(lc)
                l += 1
        return res