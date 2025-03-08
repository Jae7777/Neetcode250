# https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            digit = (columnNumber - 1) % 26
            res.append(chr(ord('A') + digit))
            columnNumber -= digit
            columnNumber = columnNumber // 26
        return "".join(res[::-1])