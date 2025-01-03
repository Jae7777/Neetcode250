# https://neetcode.io/problems/longest-repeating-substring-with-replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        count = defaultdict(int)
        m = 0
        while r < len(s):
            lc, rc = s[l], s[r]
            count[rc] += 1
            m = max(m, count[rc])
            while (r - l + 1 - m) > k:
                count[lc] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
                    

