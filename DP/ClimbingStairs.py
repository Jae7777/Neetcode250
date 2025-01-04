# https://neetcode.io/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int: # this is just fib
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b