# https://neetcode.io/problems/minimum-window-with-characters
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        scount, tcount = defaultdict(int), defaultdict(int)
        for c in s:
            scount[c] += 1
        for c in t:
            tcount[c] += 1
        matches = 0
        for c in tcount:
            if c in scount and scount[c] >= tcount[c]:
                matches += 1
        if matches != len(tcount):
            return ""
        l, r = 0, len(s) - 1 
        while r - l + 1 > len(t):
            lc, rc = s[l], s[r]
            if lc not in tcount or scount[lc] != tcount[lc]:
                scount[lc] -= 1
                l += 1
            elif rc not in tcount or scount[rc] != tcount[rc]:
                tcount[rc] -= 1
                r -= 1
            else:
                break
        return s[l:r+1]
        