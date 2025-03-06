# https://neetcode.io/problems/minimum-window-with-characters
# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        scount, tcount = defaultdict(int), defaultdict(int)
        for c in t:
            tcount[c] += 1
        matches = 0
        l, r = 0, 0
        res = (float('inf'), float('inf'), float('inf'))
        print(tcount)
        while r < len(s):
            if matches != len(tcount):
                scount[s[r]] += 1
                if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                    matches += 1
                r += 1
            while matches == len(tcount):
                res = min(res, (r - l, l, r))
                if s[l] in tcount and scount[s[l]] == tcount[s[l]]:
                    matches -= 1
                scount[s[l]] -= 1
                l += 1
        return s[res[1] : res[2]] if res[0] != float('inf') else ""
            
        