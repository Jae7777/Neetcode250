# https://neetcode.io/problems/permutation-string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count, s2count = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1count[s1[i]] += 1
        for i in range(len(s1) - 1):
            s2count[s2[i]] += 1
        matches = 0
        for c in s1count:
            if c in s2count and s1count[c] == s2count[c]:
                matches += 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            lc, rc = s2[l], s2[r]
            if rc in s1count and s2count[rc] == s1count[rc]:
                matches -= 1
            s2count[rc] += 1
            if rc in s1count and s2count[rc] == s1count[rc]:
                matches += 1
            if matches == len(s1count):
                return True
            if lc in s1count and s2count[lc] == s1count[lc]:
                matches -= 1
            s2count[lc] -= 1
            if lc in s1count and s2count[lc] == s1count[lc]:
                matches += 1
            r += 1
            l += 1
        return False
            