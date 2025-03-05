# https://neetcode.io/problems/sum-of-two-integers
# https://leetcode.com/problems/sum-of-two-integers/description/
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_without_carry
            b = carry
        return a if a <= max_int else ~(a ^ mask)
