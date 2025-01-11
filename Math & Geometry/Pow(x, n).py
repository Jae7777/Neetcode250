# https://neetcode.io/problems/pow-x-n
# O(n) time, O(1) space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            prod = x
            for _ in range(1, n):
                prod *= x
            return prod
        if n < 0:
            prod = x
            for _ in range(1, -n):
                prod *= x
            return 1 / prod

# O(logn) time, O(logn) space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        a = self.myPow(x ** 2, abs(n) // 2) * (x if n % 2 else 1)
        return 1 / a if n < 0 else a