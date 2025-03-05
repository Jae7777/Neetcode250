# https://neetcode.io/problems/combinations-of-a-phone-number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res, combo = [], []
        def createCombo(i):
            if i >= len(digits):
                res.append("".join(combo))
                return
            for c in digitToChar[digits[i]]:
                combo.append(c)
                createCombo(i + 1)
                combo.pop()

        createCombo(0)
        return res