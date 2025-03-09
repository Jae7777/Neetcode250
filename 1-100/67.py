# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A, B = len(a), len(b)
        carry = 0
        res = []
        i = 0
        while i < A and i < B:
            total = int(a[A - i - 1]) + int(b[B - i - 1]) + carry
            digit = total & 1
            carry = total >> 1
            res.append(str(digit))
            i += 1
        while i < A:
            total = int(a[A - i - 1]) + carry
            digit = total & 1
            carry = total >> 1
            res.append(str(digit))
            i += 1
        while i < B:
            total = int(b[B - i - 1]) + carry
            digit = total & 1
            carry = total >> 1
            res.append(str(digit))
            i += 1
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])