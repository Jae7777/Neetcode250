# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        res = 0
        combo = ""
        for c in s:
            combo += c
            if len(combo) == 2:
                if combo in value:
                    res += value[combo]
                    combo = ""
                else:
                    res += value[combo[0]]
                    combo = combo[1]
        res += value[combo] if combo in value else 0
        return res