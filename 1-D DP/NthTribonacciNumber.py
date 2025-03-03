# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return a
        if n == 1:
            return b
        while n > 2:
            t = a
            a = b
            b = c
            c = t + a + b
            n -= 1
        return c