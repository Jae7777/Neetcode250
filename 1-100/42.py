# https://neetcode.io/problems/trapping-rain-water
# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            lh, rh = height[l], height[r]
            area = 0
            if lh < rh:
                ll = l + 1
                while ll < r and height[ll] < lh:
                    area += lh - height[ll]
                    ll += 1
                l = ll
            else:
                rr = r - 1
                while rr > l and height[rr] < rh:
                    area += rh - height[rr]
                    rr -= 1
                r = rr
            res += area
        return res
            
                
                