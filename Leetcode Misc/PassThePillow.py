# https://leetcode.com/problems/pass-the-pillow/
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time == 0:
            return 1
        if (time - 1) // (n - 1) % 2 == 0:
            return 2 + ((time - 1) % (n - 1))
        else:
            return n - 1 - ((time - 1) % (n - 1))