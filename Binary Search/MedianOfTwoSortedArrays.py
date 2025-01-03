# https://neetcode.io/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1, nums2
        if len(n1) > len(n2):
            n1, n2 = n2, n1
        N = len(n1) + len(n2)
        half = N // 2
        l1, r1 = 0, len(n1) - 1
        while True:
            m1 = (l1 + r1) // 2
            m2 = half - m1 - 2
            vl1 = n1[m1] if m1 >= 0 else float('-inf')
            vr1 = n1[m1 + 1] if m1 + 1 < len(n1) else float('inf')
            vl2 = n2[m2] if m2 >= 0 else float('-inf')
            vr2 = n2[m2 + 1] if m2 + 1 < len(n2) else float('inf')
            if vl1 <= vr2 and vl2 <= vr1:
                if N % 2 == 0:
                    return (max(vl1, vl2) + min(vr1, vr2)) / 2
                else:
                    return min(vr1, vr2)
            elif vl1 > vr2:
                r1 = m1 - 1
            else:
                l1 = m1 + 1