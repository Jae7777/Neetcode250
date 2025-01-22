# https://leetcode.com/problems/find-in-mountain-array/
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        peak_i = -1
        while l <= r:
            m = (l + r) // 2
            l_num = mountainArr.get(m - 1) if m - 1 >= 0 else float('-inf') 
            m_num = mountainArr.get(m)
            r_num = mountainArr.get(m + 1) if m + 1 < mountainArr.length() else float('inf')
            if l_num < m_num < r_num:
                l = m + 1
            elif l_num > m_num > r_num:
                r = m - 1
            else:
                peak_i = m
                break
        l, r = 0, peak_i
        while l <= r:
            m = (l + r) // 2
            num = mountainArr.get(m)
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return m
        l, r = peak_i + 1, mountainArr.length() - 1
        while l <= r:
            m = (l + r) // 2
            num = mountainArr.get(m)
            if num < target:
                r = m - 1
            elif num > target:
                l = m + 1
            else:
                return m
        return -1