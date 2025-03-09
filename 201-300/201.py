# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        digit = 1
        while left and right:
            diff = right - left
            if diff == 0 and left & 1 == 1 and right & 1 == 1:
                res += digit
            digit <<= 1
            left >>= 1
            right >>= 1
        return res