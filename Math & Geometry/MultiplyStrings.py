# https://neetcode.io/problems/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        digit1 = 1
        for c1 in num1[::-1]:
            n1 = int(c1)
            digit2 = 1
            for c2 in num2[::-1]:
                n2 = int(c2)
                res += n1 * n2 * digit1 * digit2
                digit2 *= 10
                print(res)
            digit1 *= 10
        return str(res)