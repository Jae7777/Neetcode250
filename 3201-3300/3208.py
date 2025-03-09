# https://leetcode.com/problems/alternating-groups-ii/description/

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        l, r = 0, 1
        res = 0
        while l < n:
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
                r += 1
            elif r - l + 1 < k:
                r += 1
            else:
                res += 1
                l += 1
                r += 1
        return res