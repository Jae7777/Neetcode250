# https://neetcode.io/problems/number-of-one-bits
# O(n) time, O(1) space
# n is the number of bits in the number
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n > 0:
            if n & 1:
                ones += 1
            n = n >> 1
        return ones