# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        l, r = 0, 0
        while r < k:
            if blocks[r] == 'W':
                whites += 1
            r += 1
        minWhites = whites
        while r < len(blocks):
            if blocks[r] == 'W':
                whites += 1
            r += 1
            if blocks[l] == 'W':
                whites -= 1
            l += 1
            minWhites = min(minWhites, whites)
        return minWhites
