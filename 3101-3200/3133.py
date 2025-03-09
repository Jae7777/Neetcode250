# https://leetcode.com/problems/minimum-array-end/\

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = n - 1
        res = x
        digit = 1
        while n:
            if not (x & digit):
                res |= (n & 1) * digit
                n >>= 1
            digit <<= 1
        return res
