# https://neetcode.io/problems/eating-bananas
# https://leetcode.com/problems/koko-eating-bananas/description/
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += -(p // -m) # ceil divide
            if time > h:
                l = m + 1
            else:
                k = min(k, m)
                r = m - 1
        return k