# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        for j in range(len(number) - 1):
            if number[j] == digit:
                if int(number[j]) < int(number[j + 1]):
                    return number[:j] + number[j+1:]
                else:
                    i = j
        if number[-1] == digit:
            return number[:-1]
        return number[:i] + number[i+1:]
