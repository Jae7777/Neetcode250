# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        i = 0
        while i < min_len:
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]