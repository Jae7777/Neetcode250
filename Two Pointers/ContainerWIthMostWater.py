# https://neetcode.io/problems/max-water-container
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            lh, rh = heights[l], heights[r]
            area = min(lh, rh) * (r - l)
            if lh < rh:
                l += 1
            else:
                r -= 1
            res = max(res, area)
        return res