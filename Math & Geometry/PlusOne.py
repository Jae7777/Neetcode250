# https://neetcode.io/problems/plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        return ([1] if carry else []) + digits

# optimal
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                return digits
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        return ([1] if carry else []) + digits