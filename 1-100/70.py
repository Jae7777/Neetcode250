# https://leetcode.com/problems/climbing-stairs/submissions/1562046000/
# 1-D DP
# TIME: O(N)
# SPACE: O(1)
class Solution:
    def climbStairs(self, n: int) -> int: # this is just fib
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b