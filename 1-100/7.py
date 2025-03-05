# https://neetcode.io/problems/reverse-integer
# https://leetcode.com/problems/reverse-integer/description/
import math
class Solution:
    def reverse(self, x: int) -> int:
        min_int = -2**31
        max_int = 2**31 - 1
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > max_int // 10 or (res == max_int // 10 and digit >= max_int % 10)):
                return 0
            if (res < min_int // 10 or (res == min_int // 10 and digit <= min_int % 10)):
                return 0
            res = res * 10 + digit
        return res